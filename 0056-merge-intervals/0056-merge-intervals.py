class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n=len(intervals)
        ans=[]
        intervals.sort()
        for i in range(n):
            start,end=intervals[i][0],intervals[i][1]
            
            if ans and end<=ans[-1][1]:
                continue
            for j in range(i+1,n):
                if intervals[j][0]<=end:
                    end=max(end,intervals[j][1])
                else:
                    break
            ans.append([start,end])
        return ans