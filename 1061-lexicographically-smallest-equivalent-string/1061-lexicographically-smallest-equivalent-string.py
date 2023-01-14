class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        D = {i: i for i in ascii_lowercase}
        def parent(x):
            if D[x] == x: return x
            x = parent(D[x])
            return x
        def union(x, y):
            u, v = parent(x), parent(y)
            D[u] = D[v] = min(u, v)
        for a, b in zip(s1, s2):
            union(a, b)
        return ''.join([parent(i) for i in baseStr])