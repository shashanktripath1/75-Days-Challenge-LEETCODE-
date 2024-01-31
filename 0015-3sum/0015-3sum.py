class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        st=set()
        n=len(nums)
        for i in range(n):
            hashset=set()
            for j in range(i+1,n):
                third=-(nums[i]+nums[j])
                if third in hashset:
                    temp=[nums[i],nums[j],third]
                    temp.sort()
                    st.add(tuple(temp))
                hashset.add(nums[j])
        return list(st)