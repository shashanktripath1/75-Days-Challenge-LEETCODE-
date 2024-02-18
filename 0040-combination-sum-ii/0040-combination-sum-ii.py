class Solution:
    def helper(self,ind,arr,target,ans,ds):
        if target==0:
            ans.append(ds[:])
            return
        for i in range(ind,len(arr)):
            if i>ind and arr[i]==arr[i-1]:
                continue
            if arr[i]>target:
                break
            ds.append(arr[i])
            self.helper(i+1,arr,target-arr[i],ans,ds)
            ds.pop()
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans=[]
        self.helper(0,candidates,target,ans,[])
        return ans