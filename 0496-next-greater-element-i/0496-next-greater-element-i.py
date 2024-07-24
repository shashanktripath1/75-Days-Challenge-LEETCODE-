class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        next_greater = {}
        st = []

        for num in nums2:
            while st and st[-1] < num:
                next_greater[st.pop()] = num
            st.append(num)
        
        while st:
            next_greater[st.pop()] = -1
        
        return [next_greater[num] for num in nums1]