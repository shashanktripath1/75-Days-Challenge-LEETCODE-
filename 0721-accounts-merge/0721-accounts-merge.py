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
    def accountsMerge(self, accounts):
        n = len(accounts)
        ds = DisjointSet(n)
        
        # Sort the accounts
        accounts.sort()
        
        # Map email to its corresponding node
        mapMailNode = {}
        for i in range(n):
            for j in range(1, len(accounts[i])):
                mail = accounts[i][j]
                if mail not in mapMailNode:
                    mapMailNode[mail] = i
                else:
                    ds.unionBySize(i, mapMailNode[mail])

        # Merge emails based on their nodes
        mergedMail = [[] for _ in range(n)]
        for mail, node in mapMailNode.items():
            node = ds.findUPar(node)
            mergedMail[node].append(mail)

        # Construct the final merged accounts
        ans = []
        for i in range(n):
            if not mergedMail[i]:
                continue
            mergedMail[i].sort()
            temp = [accounts[i][0]]
            temp.extend(mergedMail[i])
            ans.append(temp)

        # Sort the final result
        ans.sort()
        return ans
