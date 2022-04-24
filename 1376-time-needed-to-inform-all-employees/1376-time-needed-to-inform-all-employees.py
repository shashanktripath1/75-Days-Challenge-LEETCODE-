class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        def dfs(eid):
            if manager[eid]!=-1:
                informTime[eid]+=dfs(manager[eid])
                manager[eid]=-1
            return informTime[eid]
        for eid in range(n):
            dfs(eid)
        return max(informTime)