class Solution:
    def possible(self,weights,capacity):
        load=0
        days=1
        n=len(weights)
        for i in range(n):
            if load+weights[i]>capacity:
                days+=1
                load=weights[i]
            else:
                load+=weights[i]
        return days
        
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low=max(weights)
        high=sum(weights)
        #ans=low
        while low<=high:
            mid=(low+high)//2
            days_possible=self.possible(weights,mid)
            if days_possible<=days:
                #ans=mid
                high=mid-1
            else:
                low=mid+1
        return low