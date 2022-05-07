## Input file formats

### Edge list
Using [nx.parse_edgelist](https://networkx.org/documentation/stable/reference/readwrite/generated/networkx.readwrite.edgelist.parse_edgelist.html#networkx.readwrite.edgelist.parse_edgelist) function for reading data as NetworkX graph, 
```python
# from the online doc
lines = ["1 2 3", "2 3 27", "3 4 3.0"]
G = nx.parse_edgelist(lines, nodetype=int, data=(("weight", float),))
list(G)
# [1, 2, 3, 4]
list(G.edges(data=True))
# [(1, 2, {'weight': 3.0}), (2, 3, {'weight': 27.0}), (3, 4, {'weight': 3.0})]
```

## Generate random graphs
A total list of available algorithms can be found at [NetworkX doc: generators](https://networkx.org/documentation/stable/reference/generators.html)

For directed graphs, In-degree sequence and out-degree sequence are required. *compare the efficiencies of these algorithms*
- Using [nx.directed_configuration_model](https://networkx.org/documentation/stable/reference/generated/networkx.generators.degree_seq.directed_configuration_model.html#networkx.generators.degree_seq.directed_configuration_model)
- [nx.directed_havel_hakimi_graph](https://networkx.org/documentation/stable/reference/generated/networkx.generators.degree_seq.directed_havel_hakimi_graph.html#networkx.generators.degree_seq.directed_havel_hakimi_graph)

For undirected graphs, see [nx.configuration_model](https://networkx.org/documentation/stable/reference/generated/networkx.generators.degree_seq.configuration_model.html#networkx.generators.degree_seq.configuration_model), or can try other different algorithms, e.g., [nx.expected_degree_graph](https://networkx.org/documentation/stable/reference/generated/networkx.generators.degree_seq.expected_degree_graph.html#networkx.generators.degree_seq.expected_degree_graph), havel_hakimi_graph, 
