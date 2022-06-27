class Solution:
    def frequencySort(self, s: str) -> str:
        s=list(s)
        d={}
        for i in range(len(s)):
            if s[i] in d:
                d[s[i]]+=1
            else:
                d[s[i]]=1
        ans=[]
        for i in sorted(d.keys(),key=d.get,reverse=True):
            ans.append(d[i]*i)
        return "".join(ans)
        