class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans=[]
        l=len(s)
        def dfs(i,temp):
            if i==l:
                ans.append(temp)
            j=i+1
            while(j<l+1):
                if s[i:j]==s[i:j][::-1]:
                    dfs(j,temp+[s[i:j]])
                j+=1
        dfs(0,[])
        return ans
                