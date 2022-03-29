class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans,dic,currsum=0,{},0
        for i in nums:
            if currsum+i==k:
                ans+=1
            if ((currsum+i)-k)  in dic:
                ans+=dic[((currsum+i)-k)]
            currsum+=i
            dic[currsum]=dic.get(currsum,0)+1
        return ans