class Solution:
    def helper(self,i,arr,target,list1,ans):
        n=len(arr)
        if i==n:
            if target==0:
                ans.append(list1[:])
            return ans
        if arr[i]<=target:
            list1.append(arr[i])
            self.helper(i,arr,target-arr[i],list1,ans)
            list1.pop()
        return self.helper(i+1,arr,target,list1,ans)
        
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        list1,ans=[],[]
        return self.helper(0,candidates,target,list1,ans)