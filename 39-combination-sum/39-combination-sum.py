class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # ans=[]
        def helper(i,arr,target,list1, ans):
            if i==len(arr):
                if target ==0:
                    ans.append(list1[:])
                    # print(ans)
                return ans
            if arr[i]<=target:
                list1.append(arr[i])
                helper(i,arr,target-arr[i],list1, ans)
                list1.pop()
            return helper(i+1,arr,target,list1, ans)
            # return list1
        # print(ans)
        return helper(0,candidates,target,[], [])
        # print(a)

       