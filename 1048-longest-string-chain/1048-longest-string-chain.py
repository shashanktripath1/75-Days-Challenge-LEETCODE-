class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        arr = [(len(e), e) for e in words]
        arr.sort()
        d = {e:1 for e in words}
        for l, e in arr:
            self.check(e, d)
        return max(d.values())
    
    def check(self, w, d):
        for i in range(len(w)):
            s = w[:i] + w[i+1:]
            if d.get(s, False):
                d[w] = max(d[w], d[s]+1)
        return d