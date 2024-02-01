class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n=len(intervals)
        ans=[]
        intervals.sort()
        for i in range(n):
            #if current interval does not lie in the last interval
            if not ans or intervals[i][0]>ans[-1][1]:
                ans.append(intervals[i])
            #if current interval lie in the previous interval
            else:
                ans[-1][1]=max(ans[-1][1],intervals[i][1])
        return ans