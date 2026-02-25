# Support-Weighted Graph Scoring (Katz-Based Model)

## Overview

This project calculates the final importance (or "weight") of nodes in a directed graph where:

- Each node has an intrinsic (base) value.
- Nodes may support other nodes.
- Supporting valuable nodes increases your own value.
- Support can compound through the network.

The system uses a mathematically stable version of **Katz centrality** with intrinsic node values.

---

# Part 1 — Intuitive Explanation (8th Grade Level)

## The Motivation

Imagine a network where:

- Each point (node) has its own starting value.
- Some points support other points.
- Supporting something important should make you more important too.

But:

- We don’t want importance to grow forever.
- We don’t want weird loops to create infinite value.
- We want the result to be fair and predictable.

So we built a system that:

> Gives each node its base value, plus some credit for the value of what it supports.

---

## How It Works (Simple Version)

1. Every node starts with its intrinsic value.
2. If a node supports another node, it gets some credit from that node.
3. That credit is only partial (not 100%).
4. The farther away the support chain is, the smaller the credit becomes.
5. We repeat the calculation until the values stop changing.

So a node’s final value becomes:

```
Final Value =
Base Value

* Credit from directly supported nodes
* Smaller credit from indirectly supported nodes
* Even smaller credit from farther chains

```

The system ensures:

- Direct support matters most.
- Indirect support matters less.
- Very long chains matter very little.
- The numbers always settle to a stable answer.

---

## Why This Makes Sense

- You keep your original value.
- You gain value by supporting valuable things.
- Longer chains matter less and less.
- The system cannot “blow up” or run forever.

In short:

> A node becomes important if it supports important nodes — but influence fades with distance.

---

# Part 2 — Technical Explanation (More Thorough)

## Mathematical Model

Let:

- \( V_i \) = intrinsic value of node \( i \)
- \( x_i \) = final computed value of node \( i \)
- \( w_{ij} \) = strength of support from node \( i \) to node \( j \)
- \( \alpha \in (0,1) \) = damping factor

We define:

\[
x_i = V_i + \alpha \sum_j w_{ij} x_j
\]

In matrix form:

\[
x = V + \alpha W x
\]

Solving:

\[
x = (I - \alpha W)^{-1} V
\]

This is a standard Katz centrality formulation with a node-specific base term.

---

## Interpretation as a Series

The solution expands to:

\[
x = V + \alpha W V + \alpha^2 W^2 V + \alpha^3 W^3 V + \cdots
\]

Meaning:

- \( V \): intrinsic value
- \( \alpha W V \): credit from direct support
- \( \alpha^2 W^2 V \): credit from two-step chains
- \( \alpha^3 W^3 V \): credit from three-step chains
- etc.

Each additional step is discounted by another factor of \( \alpha \).

This guarantees:

- Longer chains contribute less.
- Infinite loops shrink geometrically.
- Total value remains bounded.

---

## Budgeted Support (Normalization)

To prevent nodes with many outgoing edges from having artificial influence, we optionally normalize outgoing weights:

\[
w_{ij} = \frac{s_{ij}}{\sum_k s_{ik}}
\]

This ensures each node distributes a fixed support budget.

---

## Stability and Convergence

If weights are nonnegative and \( \alpha < 1 \), the system:

- Converges to a unique fixed point.
- Is monotonic (increasing intrinsic values cannot reduce scores).
- Cannot diverge or oscillate indefinitely.

We compute the result using iterative updates:

\[
x^{(t+1)} = V + \alpha W x^{(t)}
\]

until:

```

max difference between iterations < small tolerance

```

---

## Design Guarantees

This model provides:

- **Local interpretability** — A node's score is directly tied to who it supports.
- **Global consistency** — All nodes are evaluated under the same rule.
- **Path transparency** — Influence is the sum of discounted support chains.
- **Bounded influence** — Long cycles cannot inflate values infinitely.
- **Comparability** — Normalization makes support fair across nodes.

---

# Summary

This system combines:

- Intrinsic node value
- Structured support relationships
- Controlled compounding through a damping factor
- Mathematical guarantees of stability

It produces a final score that reflects both:

- Individual merit
- Network-based reinforcement

while remaining stable, explainable, and computationally reliable.

