class DisjointSet:
    def __init__(self, n):
        self.rank = [0] * (n + 1)
        self.parent = [i for i in range(n + 1)]
        self.size = [1] * (n + 1)

    def findUPar(self, node):
        if node == self.parent[node]:
            return node
        self.parent[node] = self.findUPar(self.parent[node])
        return self.parent[node]

    def unionByRank(self, u, v):
        ulp_u = self.findUPar(u)
        ulp_v = self.findUPar(v)
        if ulp_u == ulp_v:
            return
        if self.rank[ulp_u] < self.rank[ulp_v]:
            self.parent[ulp_u] = ulp_v
        elif self.rank[ulp_v] < self.rank[ulp_u]:
            self.parent[ulp_v] = ulp_u
        else:
            self.parent[ulp_v] = ulp_u
            self.rank[ulp_u] += 1

    def unionBySize(self, u, v):
        ulp_u = self.findUPar(u)
        ulp_v = self.findUPar(v)
        if ulp_u == ulp_v:
            return
        if self.size[ulp_u] < self.size[ulp_v]:
            self.parent[ulp_u] = ulp_v
            self.size[ulp_v] += self.size[ulp_u]
        else:
            self.parent[ulp_v] = ulp_u
            self.size[ulp_u] += self.size[ulp_v]

class Solution:
    def removeStones(self, stones):
        n=len(stones)
        # Finding the maximum row and column values
        maxRow = 0
        maxCol = 0
        for it in stones:
            if it[0] > maxRow:
                maxRow = it[0]
            if it[1] > maxCol:
                maxCol = it[1]
        # Initializing a Disjoint Set to represent connected components
        ds = DisjointSet(maxRow + maxCol + 1)
        stoneNodes = {}
        # Union operation for stones in the same row or column
        for it in stones:
            nodeRow = it[0]
            nodeCol = it[1] + maxRow + 1
            ds.unionBySize(nodeRow, nodeCol)
            stoneNodes[nodeRow] = 1
            stoneNodes[nodeCol] = 1
        # Counting the number of connected components

        cnt = 0
        for it in stoneNodes:
            if ds.findUPar(it) == it:
                cnt += 1
        # Calculating the maximum number of stones that can be removed
        return n - cnt


        