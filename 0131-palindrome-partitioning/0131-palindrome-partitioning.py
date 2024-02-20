class Solution:
    def is_palindrome(self,s,start,end):
        while start<=end:
            if s[start]!=s[end]:
                return False
            start+=1
            end-=1
        return True
    def helper(self,ind,res,path,s):
        if ind==len(s):
            res.append(path.copy())
            return
        for i in range(ind,len(s)):
            if self.is_palindrome(s,ind,i)==True:
                path.append(s[ind:i+1])
                self.helper(i+1,res,path,s)
                path.pop()
    def partition(self, s: str) -> List[List[str]]:
        res,path=[],[]
        self.helper(0,res,path,s)
        return res