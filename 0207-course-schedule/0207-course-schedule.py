class Solution:
    def canFinish(self, num: int, pre: List[List[int]]) -> bool:
        graph = defaultdict(list)
        incoming = [0]*num
        for u, v in pre :
            incoming[v] += 1
            graph[u].append(v)
        q = []
        for v in range(num) :
            if  incoming[v] == 0 :
                q.append(v)
        if not q : return False
        cnt = 0
        while q :
            u = q.pop()
            cnt += 1
            for v in graph[u] :
                incoming[v] -= 1
                if incoming[v] == 0 :
                    q.append(v)
        return cnt == num