class Solution(object):
    def merge(self, intervals):
        
        intervals = sorted(intervals,key=lambda l:l[0])
        
        res = []
        
        [cur1,cur2] = intervals.pop(0)
        while intervals:
            [pr1,pr2] = intervals.pop(0)
            if pr1<=cur2:
                cur2 = max(cur2, pr2)
            else:
                res.append([cur1, cur2])
                [cur1,cur2] = [pr1,pr2]

        
        res.append([cur1, cur2])

        return res  
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        