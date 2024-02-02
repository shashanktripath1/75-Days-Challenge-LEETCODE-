class Solution:
    def countPairs(self,arr,low,mid,high):
        right=mid+1
        count=0
        for i in range(low,mid+1):
            while right<=high and arr[i] > 2 * arr[right]:
                right+=1
            count+=(right-(mid+1))
        return count
    def merge(self,arr,low,mid,high):
        temp=[]
        left=low
        right=mid+1
        while left<=mid and right<=high:
            if arr[left]<=arr[right]:
                temp.append(arr[left])
                left+=1
            else:
                temp.append(arr[right])
                right+=1
        while left<=mid:
            temp.append(arr[left])
            left+=1
        while right<=high:
            temp.append(arr[right])
            right+=1
        for i in range(low,high+1):
            arr[i]=temp[i-low]

    def merge_sort(self,arr,low,high):
        count=0
        if low>=high:
            return count
        mid=(low+high)//2
        count+=self.merge_sort(arr,low,mid)
        count+=self.merge_sort(arr,mid+1,high)
        count+=self.countPairs(arr,low,mid,high)
        self.merge(arr,low,mid,high)
        return count
        
        
        
    def reversePairs(self, nums: List[int]) -> int:
        n=len(nums)
        return self.merge_sort(nums,0,n-1)