class Solution:
    def __init__(self):
        # Initialize timer for DFS
        self.timer = 1

    def dfs(self, node, parent, vis, adj, tin, low, bridges):
        # Mark current node as visited
        vis[node] = 1
        # Initialize discovery time and low value
        tin[node] = low[node] = self.timer
        self.timer += 1
        # Traverse all adjacent nodes
        for it in adj[node]:
            # Skip parent node
            if it == parent:
                continue
            # If node is not visited
            if vis[it] == 0:
                # Recursive DFS call
                self.dfs(it, node, vis, adj, tin, low, bridges)
                # Update low value
                low[node] = min(low[it], low[node])
                # If there is a bridge, add it to the list
                if low[it] > tin[node]:
                    bridges.append([it, node])
            else:
                # Update low value
                low[node] = min(low[node], low[it])

    def criticalConnections(self, n, connections):
        # Initialize adjacency list
        adj = [[] for _ in range(n)]
        # Construct adjacency list from connections
        for u, v in connections:
            adj[u].append(v)
            adj[v].append(u)
        # Initialize arrays for DFS
        vis = [0] * n
        tin = [0] * n
        low = [0] * n
        bridges = []  # List to store bridges
        # Perform DFS
        self.dfs(0, -1, vis, adj, tin, low, bridges)
        return bridges

