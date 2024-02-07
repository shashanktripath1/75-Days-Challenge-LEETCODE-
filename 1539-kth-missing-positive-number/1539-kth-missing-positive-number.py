class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        n=len(arr)
        for i in range(n):
            if arr[i]<=k:
                k+=1
            else:
                break
        return k