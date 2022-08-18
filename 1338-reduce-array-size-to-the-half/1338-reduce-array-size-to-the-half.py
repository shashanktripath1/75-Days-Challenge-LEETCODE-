class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        d={}
        for i in arr:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        lst=list(d.values())
        lst.sort(reverse=True)
        ans,count,index,size=0,0,0,len(arr)
        while(count*2<size):
            ans+=1
            count+=lst[index]
            index+=1
        return ans