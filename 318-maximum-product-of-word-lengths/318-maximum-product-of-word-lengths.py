class Solution:
    def maxProduct(self, words: List[str]) -> int:
        def shareCommon(w1,w2):
            for c in w1:
                if c in w2: return True
            return False

        N = len(words)
        mx = 0
    
        for i in range(N-1):
            for j in range(i+1, N):
                if not shareCommon(words[i], words[j]):
                    mx = max(mx, len(words[i]) * len(words[j]))

        return mx