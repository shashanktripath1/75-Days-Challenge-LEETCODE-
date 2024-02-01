class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n=len(nums)
        st=set()
        for i in range(n):
            for j in range(i+1,n):
                hashmap=set()
                for k in range(j+1,n):
                    first_three=nums[i]+nums[j]+nums[k]
                    left_one=target-first_three
                    if left_one in hashmap:
                        temp=[nums[i],nums[j],nums[k],left_one]
                        temp.sort()
                        st.add(tuple(temp))
                    hashmap.add(nums[k])
        return [list(i) for i in st]
                            