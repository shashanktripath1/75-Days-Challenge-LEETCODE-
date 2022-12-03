class Solution:
    def frequencySort(self, s: str) -> str:
        d={}
        for i in s:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        
        d1=sorted(d.items(),key=lambda x:(-x[1],x[0]))
        words=[i*j for i,j in d1]
        return "".join(words)