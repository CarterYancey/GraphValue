import networkx as nx

# Build directed graph with edge weights = support strengths s_ij
G = nx.DiGraph()
G.add_weighted_edges_from([
    (8,3,2.0), (8,4,1.0), (8,1,1.0),
    (4,1,1.0), (4,2,1.0),
    (5,1,1.0), (5,4,1.0), (5,2,1.0),
    (6,3,1.0), (6,7,1.0), (6,5,1.0),
    (7,3,1.0), (7,5,1.0),
])

# Intrinsic values V_i
V = {1: 0.34, 2: 0.21, 3: 0.13, 4: 0.08, 5: 0.05, 6: 0.03, 7: 0.02, 8: 0.01}
print("V: ", V)
nx.nx_agraph.to_agraph(G).draw("graph.png", prog="dot")

alpha = 0.8  # choose < 1/lambda_max for convergence (NetworkX notes this)
x = nx.katz_centrality(G, alpha=alpha, beta=V, weight="weight", normalized=False)
print("x: ", x)
for n in G.nodes():
    G.nodes[n]["label"] = f"{n}\n{round(katz[n],3)}"

nx.nx_agraph.to_agraph(G).draw("katz_graph.png", prog="dot")
