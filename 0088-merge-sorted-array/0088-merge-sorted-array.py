class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        left,right=m-1,0
        while left>=0 and right<n:
            if nums1[left]>nums2[right]:
                nums1[left],nums2[right]=nums2[right],nums1[left]
                left-=1
                right+=1
            else:
                break
       
        nums1[m:]=nums2[:n]
        nums1.sort()
        return nums1
        
        