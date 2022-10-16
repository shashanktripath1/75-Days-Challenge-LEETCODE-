class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
                
        indegree=[0]*(numCourses)
        graph=defaultdict(list)
        res=[]
        for courses in prerequisites:
            graph[courses[1]].append(courses[0])
            indegree[courses[0]] += 1
        queue=deque()

        for v in range(numCourses):
            if indegree[v]==0:
                queue.append(v)
        while queue:
            u=queue.popleft()
            res.append(u)
            for v in graph[u]:
                indegree[v]-=1
                if indegree[v]==0:
                    queue.append(v)
        if len(res)==numCourses:
            return res
        return []
            