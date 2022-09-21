class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        S=0
        for i in nums:
            if i%2==0:
                S+=i
        res=[]
        for fir,sec in queries:
            if nums[sec]%2==0:
                S-=nums[sec]
            nums[sec]+=fir
            if nums[sec]%2==0:
                S+=nums[sec]
            res.append(S)
        return res