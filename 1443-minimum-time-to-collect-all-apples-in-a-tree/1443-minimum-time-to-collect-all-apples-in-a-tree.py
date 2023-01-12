class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        def kahnsalgo():
            N = len(hasApple)
            E = len(edges)
            indegrees = [0] * N
            
            for u,v in edges:
                indegrees[v] += 1
                indegrees[u] += 1
            
            queue = deque()
            for i,ind in enumerate(indegrees):
                if ind == 1 and not hasApple[i]: # if there's only 1 in-edge and there's no apple -> empty leaf
                    queue.append(i) # add for removal
                    
            removed_nodes = 0
            while queue:
                node = queue.popleft()
                
                if node == 0: # we cannot remove root in any case
                    continue
                
                for nei in adj_list[node]:
                    adj_list[nei].discard(node)
                    indegrees[nei] -= 1 # remove edge from v,u
                    if indegrees[nei] == 1 and not hasApple[nei]: # another leaf? add to remove
                        queue.append(nei)
                    removed_nodes += 1 # count removed nodes
            
            return (E - removed_nodes) * 2 # (all edges - edges_to_empty_nodes) * 2
        
        adj_list = defaultdict(set)
        for u,v in edges: adj_list[u].add(v), adj_list[v].add(u)
        return kahnsalgo()