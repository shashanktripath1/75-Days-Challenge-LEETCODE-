class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        d=collections.Counter(arr)
        l=list(d.values())
        l.sort(reverse=True)
        ans,count,index=0,0,0
        while(count*2<len(arr)):
            ans+=1
            count+=l[index]
            index+=1
        return ans