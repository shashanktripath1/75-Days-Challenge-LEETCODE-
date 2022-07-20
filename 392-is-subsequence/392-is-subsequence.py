class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        stack=[]
        for i in s:
            stack.append(i)
        count=0
        n=len(t)
        for i in range(n-1,-1,-1):
            if not stack:
                return True
            if t[i]==stack[-1]:
                stack.pop()
        return stack==[]