class Solution:
    def dfs(self,node,adj_list,visited):
        visited[node]=1
        for neighbour in adj_list[node]:
            if not visited[neighbour]:
                self.dfs(neighbour,adj_list,visited)
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n=len(isConnected)
        adj_list=[[] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if isConnected[i][j]==1 and i!=j:
                    adj_list[i].append(j)
                    adj_list[j].append(i)
        visited=[0]*(n+1)
        count=0
        for i in range(n):
            if not visited[i]:
                count+=1
                self.dfs(i,adj_list,visited)
        return count