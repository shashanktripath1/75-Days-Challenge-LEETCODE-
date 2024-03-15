class Solution:
    def dfs(self, node, col, color, graph):
        color[node] = col

        # Traverse adjacent nodes
        for neighbor in graph[node]:
            # If uncolored
            if color[neighbor] == -1:
                if not self.dfs(neighbor, 1 - col, color, graph):
                    return False
            # If previously colored and have the same color
            elif color[neighbor] == col:
                return False

        return True

    def isBipartite(self, graph: List[List[int]]):
        color = [-1] * len(graph)
        # For connected components
        for i in range(len(graph)):
            if color[i] == -1:
                if not self.dfs(i, 0, color, graph):
                    return False
        return True
