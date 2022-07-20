class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        def issubseq(s,t):
            stack=[]
            for i in t:
                stack.append(i)
            n=len(s)                
            for i in range(n-1,-1,-1):
                if not stack:
                    return True
                if s[i]==stack[-1]:
                    stack.pop()
            return stack==[]
        count=0
        d={}
        for i in words:
            if i not in d:
                if issubseq(s,i):
                    count+=1
                    d[i]=True
                else:
                    d[i]=False
            else:
                if d[i]:
                    count+=1
        return count