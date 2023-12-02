"""
Muhammad Shike
CS 412 Lab: Maxflow and Min cut

Implement the Ford/Fulkerson augmenting-path algorithm for computing the
max flow of a graph. 
"""

import queue

# Implementing the Ford-Fulkerson algorithm

def dfs(G, s, t):
    """
    Depth first search for finding augmenting paths in the flow network
    """
    bag = queue.LifoQueue()
    bag.put((None, s))
    dfs_parents = {}
    while not bag.empty() and dfs_parents.get(t) is None:
        p, u = bag.get()
        if u not in dfs_parents:
            dfs_parents[u] = p 
            for v in G[u]:
                # Only consider the edge if it has remaining capacity
                if G[u][v][0] < G[u][v][1]:
                    bag.put((u,v))
    return dfs_parents

def find_path(parents, t):
    """
    Reconstruct the path from the source to the sink t using the parent pointers
    """
    path = []
    node = t
    while node is not None:
        path.append(node)
        node = parents.get(node)
    path.reverse()
    return path

def min_capacity(G, path):
    """
    Returns the minimum residual capacity of the edges along the path
    """
    min_cap = float('inf')
    for i in range(len(path) - 1):
        u, v = path[i], path[i+1]
        min_cap = min(min_cap, G[u][v][1] - G[u][v][0])
    return min_cap

def update_flow(G, path, flow):
    """
    Updates the flow along the given path by the specified amount
    """
    for i in range(len(path) - 1):
        u, v = path[i], path[i+1]
        # Increase the flow on the forward edge
        G[u][v][0] += flow
        # Decrease the flow on the reverse edge, or create it if it doesn't exist
        if v not in G or u not in G[v]:
            if v not in G:
                G[v] = {}
            G[v][u] = [0, 0]
        G[v][u][0] -= flow

def ford_fulkerson(G, s, t):
    """
    Ford-Fulkerson algorithm to compute the maximum flow of the graph G
    """
    max_flow = 0
    while True:
        parents = dfs(G, s, t)
        if t not in parents:
            # No augmenting path found, so we're done
            break
        path = find_path(parents, t)
        flow = min_capacity(G, path)
        update_flow(G, path, flow)
        max_flow += flow
    return max_flow

def min_cut_edges(G, s):
    """
    Determine the edges that are in the min-cut of the flow network
    """
    parents = dfs(G, s, None) # Run DFS to determine the reachable vertices
    min_cut = []
    for u in parents:
        for v in G[u]:
            if v not in parents and G[u][v][0] == G[u][v][1]:
                # Edge is saturated and leads to a vertex not reachable from s
                min_cut.append((u, v))
    return min_cut

def main():
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
    min_cut = min_cut_edges(adj_list, s)
    
    # Output the total flow
    print(max_flow)
    # Output the edges that cross the min cut, sorted by their vertex ID
    for u, v in sorted(min_cut):
        print(u, v)
        

if __name__ == "__main__":
    main()
