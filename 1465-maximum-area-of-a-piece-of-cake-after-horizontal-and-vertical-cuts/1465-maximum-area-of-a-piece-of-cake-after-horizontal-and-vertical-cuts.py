class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts.append(0)
        horizontalCuts.append(h)
        verticalCuts.append(0)
        verticalCuts.append(w)
        horizontalCuts.sort()
        verticalCuts.sort()
        s,t=0,0
        for i in range(1,len(horizontalCuts)):
            s=max(s,horizontalCuts[i]-horizontalCuts[i-1])
        for j in range(1,len(verticalCuts)):
            t=max(t,verticalCuts[j]-verticalCuts[j-1])
        return (s*t)%1000000007
