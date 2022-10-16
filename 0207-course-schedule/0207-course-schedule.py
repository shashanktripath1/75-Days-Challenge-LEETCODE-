class Solution:
    def canFinish(self, num: int, pre: List[List[int]]) -> bool:
        graph=defaultdict(list)
        indegree=[0]*num
        for u,v in pre:
            indegree[v]+=1
            graph[u].append(v)
        queue=deque()
        for v in range(num):
            if indegree[v]==0:
                queue.append(v)
        count=0
        while queue:
            u=queue.popleft()
            count+=1
            for v in graph[u]:
                indegree[v]-=1
                if indegree[v]==0:
                    queue.append(v)
        return count==num