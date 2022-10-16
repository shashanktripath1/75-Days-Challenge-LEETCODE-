class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        arr=[]
        for i in nums:
            arr.append(int(str(i)[::-1]))
        return len(set(nums+arr))