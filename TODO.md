## TODO: Code improvements

* [ ] Add type hints throughout; run `mypy` in CI.
* [ ] Add convergence controls:

  * `tol`, `max_iter`
  * detect non-convergence and print actionable diagnostics
* [ ] Make normalization optional and explicit: `--normalize {none,row}`.
* [ ] Add “sink” handling strategy (nodes with no outgoing edges):

  * keep as zero-outflow (current)
  * or distribute to self / uniform (configurable)

## TODO: Features to add

### Explainability / Trust features (high priority)

* [ ] “Explain my score” for a selected node:

  * top contributing supported nodes (1-hop)
  * top contributing paths up to length K (2–5 hops)
  * show numeric contribution per path (product of weights × alpha^k × V source)
* [ ] Delta report:

  * show `x - V` per node and rank by boost
  * show rank changes vs intrinsic-only ordering
* [ ] Contribution breakdown charts:

  * pie/stacked bars: intrinsic vs 1-hop vs 2-hop vs 3+ hop contributions
* [ ] Parameter sensitivity:

  * sweep alpha and show how rankings change
  * highlight nodes most sensitive to alpha/weights

### Input/output formats

* [ ] Load edges/weights from:

  * CSV
  * JSON/YAML
  * Graphviz DOT (including edge labels)
* [ ] Export results to:

  * CSV (node, V, x, delta, rank)
  * JSON (full model spec + results)
  * annotated DOT (labels embedded) for external Graphviz rendering

### Visualization

* [ ] Generate side-by-side “before vs after” images automatically.
* [ ] Color nodes by:

  * final score
  * boost (`x - V`)
  * percent boost (`(x-V)/V`)
* [ ] Scale node size by final score; optionally edge thickness by weight.
* [ ] Create an interactive HTML visualization (pyvis / d3) with hover tooltips.

### Model extensions

* [ ] Support negative weights (with safeguards) or explicitly disallow them.
* [ ] Add time-based simulation (values evolving over steps) for “what-if” scenarios.
* [ ] Add alternative centralities for comparison (PageRank, eigenvector, hub/authority).

### UX / CLI

* [ ] `katz-score render --before --after` one command.
* [ ] `katz-score explain NODE_ID` to print an explanation tree.
* [ ] `katz-score sweep-alpha --min 0.1 --max 0.95 --steps 20`.
* [ ] Add a config file (`.toml`/`.yaml`) for repeatable runs.
* [ ] Provide example datasets and a tutorial notebook.
* [ ] Add reproducibility section in README (parameter logging, deterministic runs).

