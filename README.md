# Max Flow Solution for Capacity Improvement

## Overview
This GitHub repository presents an advanced implementation of the Ford-Fulkerson algorithm, a cornerstone in network flow theory, applied to optimize production capacity in a manufacturing context. Developed as part of a CS 412 lab assignment, this project serves as a demonstration of applying theoretical computer science concepts to practical, real-life problems.

## Preview

![Screenshot 2023-12-01 192835](https://github.com/MuhammadK8/cs412-maxflow/assets/144934871/95c10364-7f2c-420c-b522-788878a4fbe2)
![Recording 2023-12-01 193410](https://github.com/MuhammadK8/cs412-maxflow/assets/144934871/024f1fe4-553e-47c1-b01c-fd3886d5d1ca)

## Implementation Details

### Depth-First Search (DFS) for Finding Augmenting Paths
The implementation begins with a depth-first search (DFS) function. DFS is used to explore the network and find paths from the source node to the sink node, which are crucial for determining the flow in the network.

```python
def dfs(G, s, t):
    """
    Depth first search for finding augmenting paths in the flow network.
    """
    bag = queue.LifoQueue()
    bag.put((None, s))
    dfs_parents = {}
    while not bag.empty() and dfs_parents.get(t) is None:
        p, u = bag.get()
        if u not in dfs_parents:
            dfs_parents[u] = p 
            for v in G[u]:
                if G[u][v][0] < G[u][v][1]:  # Checking capacity
                    bag.put((u,v))
    return dfs_parents
```

### The Ford-Fulkerson Method
The Ford-Fulkerson method is the core of this implementation. It repeatedly finds augmenting paths using DFS and then updates the flow in the network until no more augmenting paths can be found, thus determining the maximum flow.

```python
def ford_fulkerson(G, s, t):
    """
    Ford-Fulkerson algorithm to compute the maximum flow of the graph G.
    """
    max_flow = 0
    while True:
        parents = dfs(G, s, t)
        if t not in parents:
            break
        path = find_path(parents, t)
        flow = min_capacity(G, path)
        update_flow(G, path, flow)
        max_flow += flow
    return max_flow
```

### Example Usage in a Network Flow Context
This snippet demonstrates how the algorithm can be applied to a network flow problem. Here, the network is defined with vertices, edges, and capacities, after which the Ford-Fulkerson algorithm is used to calculate the maximum flow.

```python
vertex_count, edge_count = [int(x) for x in input().split()]
adj_list = {}
for i in range(vertex_count):
    adj_list[i] = {}

for _ in range(edge_count):
    u, v, cap = [int(x) for x in input().split()]
    adj_list[u][v] = [0, cap]

s = 0    
t = vertex_count - 1

max_flow = ford_fulkerson(adj_list, s, t)
print("Maximum flow:", max_flow)
```

## Real-World Application
This algorithm has significant applications in areas like optimizing network data throughput, managing supply chain logistics, and efficient resource distribution in utilities.

### Custom Optimizations
- **Efficient Path Finding**: The algorithm is optimized to reduce the complexity of finding new augmenting paths.
- **Memory Management**: Careful handling of data structures to ensure memory efficiency during large-scale computations.

## Skills and Challenges
### Algorithm Complexity
- **Balancing Theory and Practice**: Implementing a complex algorithm like Ford-Fulkerson and optimizing it for real-world scenarios required a deep understanding of both theoretical and practical aspects of computer science.
- **Debugging and Testing**: Rigorous testing was required to ensure the algorithm's correctness, especially in edge cases.

### Advanced Programming Techniques
- **Data Structures**: Effective use of advanced data structures to manage complex network flows.
- **Python Proficiency**: Demonstrated advanced proficiency in Python, particularly in handling intricate algorithmic challenges.
- 
## Running the Program
1. Clone this repository to your local machine.
2. Run the `Max Flow.py` script in a Python 3 environment.
3. Input the network graph data as prompted (number of vertices, number of edges, and capacities for each edge).
