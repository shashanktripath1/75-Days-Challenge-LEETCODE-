class Solution:
    def possible(self,arr,day,m,k):
        n=len(arr)
        cnt=0
        NoOfB=0
        for i in range(n):
            if arr[i]<=day:
                cnt+=1
            else:
                NoOfB += cnt//k
                cnt=0
        NoOfB += cnt//k
        return NoOfB>=m

            
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        val=m*k
        n=len(bloomDay)
        if val>n:
            return -1
        mini=float('inf')
        maxi=float('-inf')
        for i in range(n):
            mini=min(mini,bloomDay[i])
            maxi=max(maxi,bloomDay[i])
        low,high=mini,maxi
        while low<=high:
            mid=(low+high)//2
            if self.possible(bloomDay,mid,m,k):
                high=mid-1
            else:
                low=mid+1
        return low