class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color=[-1]*len(graph)
        for i in range(len(graph)):
            if color[i]==-1:
                color[i]=1
                queue=deque()
                queue.append(i)
                while queue:
                    cur=queue.popleft()
                    for node in graph[cur]:
                        if color[node]==-1:
                            color[node]=1-color[cur]
                            queue.append(node)
                        elif color[node]==color[cur]:
                            return False
        return True