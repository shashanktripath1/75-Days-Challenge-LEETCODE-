class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1,n2=len(nums1),len(nums2)
        temp=[]
        i,j=0,0
        while i<n1 and j<n2:
            if nums1[i]<nums2[j]:
                temp.append(nums1[i])
                i+=1
            else:
                temp.append(nums2[j])
                j+=1
        temp.extend(nums1[i:])
        temp.extend(nums2[j:])
        n=n1+n2
        if n%2==1:
            return float(temp[n//2])
        median=(temp[n//2]+temp[(n//2)-1])/2.0
        return median
        
            