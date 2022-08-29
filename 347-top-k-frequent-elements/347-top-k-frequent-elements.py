class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        heap=[]
        for i in d:
            heappush(heap,(-d[i],i))
        ans=[]
        for i in range(k):
            pop=heappop(heap)
            ans.append(pop[1])
        return ans
        
        
        
        
        
        
        
        
        