import networkx as nx

# ----------------------------
# Build directed graph
# ----------------------------
G = nx.DiGraph()

edge_weights = {
    (1,4): 0.8,
    (1,5): 0.1,
    (1,8): 0.5,

    (2,4): 0.8,
    (2,5): 0.1,

    (3,6): 0.5,
    (3,7): 0.3,
    (3,8): 0.8,

    (4,1): 0.1,
    (4,5): 0.1,
    (4,8): 0.3,

    (5,4): 0.1,
    (5,6): 0.2,
    (5,7): 0.1,

    (6,4): 0.3,

    (7,6): 0.8,
}

node_names = {
        1: "Meaningful Work",
        2: "Comfort/pleasure",
        3: "Virtue",
        4: "Wealth",
        5: "Health",
        6: "Family",
        7: "Community",
        8: "SKEW"
    }

for (u,v), w in edge_weights.items():
    G.add_edge(u, v, weight=w)

# ----------------------------
# Intrinsic values
# ----------------------------
V = {1: 34, 2: 21, 3: 13, 4: 8,
     5: 3, 6: 2, 7: 1, 8: 5}

# ----------------------------
# Row-normalize (budgeted support)
# ----------------------------
'''
for n in G.nodes():
    out_edges = list(G.out_edges(n, data=True))
    total = sum(d["weight"] for _,_,d in out_edges)
    if total > 0:
        for u,v,d in out_edges:
            d["weight"] /= total
'''
# ----------------------------
# GRAPH 1: Intrinsic only
# ----------------------------
G_intrinsic = G.copy()

for n in G_intrinsic.nodes():
    G_intrinsic.nodes[n]["label"] = f"{node_names[n]}\nV={V[n]:.3f}"

for u,v,d in G_intrinsic.edges(data=True):
    d["label"] = f"{d['weight']:.3f}"

A1 = nx.nx_agraph.to_agraph(G_intrinsic)
A1.layout("dot")
A1.draw("graph_intrinsic.png")


# ----------------------------
# Compute Katz (compound support)
# ----------------------------
alpha = 1
katz = nx.katz_centrality(
    G,
    alpha=alpha,
    beta=V,
    weight="weight",
    normalized=False
)
sorted_katz = dict(sorted(katz.items(), key=lambda item: item[1]))
print("sorted_katz: ", sorted_katz)

# ----------------------------
# GRAPH 2: After Katz
# ----------------------------
G_katz = G.copy()

for n in G_katz.nodes():
    G_katz.nodes[n]["label"] = (
        f"{node_names[n]}\n"
        f"V={V[n]:.3f}\n"
        f"x={katz[n]:.3f}"
    )

for u,v,d in G_katz.edges(data=True):
    d["label"] = f"{d['weight']:.3f}"

A2 = nx.nx_agraph.to_agraph(G_katz)
A2.layout("dot")
A2.draw("graph_katz.png")

print("Saved:")
print(" - graph_intrinsic.png")
print(" - graph_katz.png")
