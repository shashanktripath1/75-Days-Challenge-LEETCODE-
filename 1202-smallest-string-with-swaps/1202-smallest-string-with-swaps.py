class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        # Store roots of each index (letter in the string). Initially each index is a root of itself
        roots = [i for i in range(len(s))]
        # Rank for each index. Initially each index has rank 1
        ranks = [1]*len(s)
        
        result = ['']*len(s)
        
        # Find root of a index 
        def find(i: int) -> int:
            while roots[i] != i:
                i = roots[i]
            return i
        
        # Inite 2 indexes. 
        # Note, without ranks I'm getting Time Limit Exeeded
        def union(x: int, y: int):
            root_x = find(x)
            root_y = find(y)
            if root_x != root_y:
                if ranks[root_x] >= ranks[root_y]:
                    roots[root_y] = root_x
                    ranks[root_x] += ranks[root_y]
                else:                    
                    roots[root_x] = root_y
                    ranks[root_y] += ranks[root_x]
        
        # Step 1: Assign roots by uniting each pair 
        for p in pairs:
            union(p[0], p[1])
        
        # Step 2: Create groups of with the same root 
        mapping = collections.defaultdict(list)
        for index in range(len(s)):
            root = find(index)
            mapping[root].append(index)

        # Step 3: Build `result` array
        for v in mapping.values():
            # Build and sort substring out of same-root group
            substring = []
            for index in v:
                substring.append(s[index])
            substring.sort()
            # Insert elements into `result` array            
            for i in range(len(substring)):
                result[v[i]] = substring[i]
                
        # Step 4: Convert array to string and return
        return "".join(result)