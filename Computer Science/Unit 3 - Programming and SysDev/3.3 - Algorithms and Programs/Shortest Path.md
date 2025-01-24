**Dijkstra’s algorithm** - Used to find the shortest path between nodes in a graph. 
A graph here means a set of objects known as nodes (or vertices). The nodes in the graph are connected by edges. These edges have a weighting – a value. The weights on the graph are a conceptual value and do not necessarily represent distance, the purpose of the shortest path algorithm is to reach a given goal node from a given start node

**Method**
- Calculate the distance of start node to all connected nodes.
- For each node, recursively calculate distance from each connected node to the start node, if it is less than currently recorded, record the length from start node and the previous node. 