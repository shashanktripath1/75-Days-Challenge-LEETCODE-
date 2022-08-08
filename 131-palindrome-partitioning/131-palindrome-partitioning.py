class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res=[]
        l=len(s)
        def dfs(i,ds):
            if i==l:
                res.append(ds)
            j=i+1
            while (j<l+1):
                if s[i:j]==s[i:j][::-1]:
                    dfs(j,ds+[s[i:j]])
                j+=1
        dfs(0,[])
        return res