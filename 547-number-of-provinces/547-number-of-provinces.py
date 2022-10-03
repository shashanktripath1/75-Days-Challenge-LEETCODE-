class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n=len(isConnected)
        adj_list=defaultdict(list)
        for row in range(n):
            for col in range(row+1,n):
                if isConnected[row][col]==1:
                    adj_list[row+1].append(col+1)
                    adj_list[col+1].append(row+1)
        def dfs(city):
            if city  in visited:
                return False
            visited.add(city)
            neighbours=adj_list[city]
            for padosi in neighbours:
                dfs(padosi)
            return True
        visited=set()
        provinces=0
        for city in range(1,n+1):
            if city not in visited and dfs(city):
                provinces+=1
        return provinces
                    