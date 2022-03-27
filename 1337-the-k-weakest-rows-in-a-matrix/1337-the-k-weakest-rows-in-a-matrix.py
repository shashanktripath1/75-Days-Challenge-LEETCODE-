from collections import defaultdict
class Solution(object):
    def kWeakestRows(self, mat, k):
        d=defaultdict(list)
        for row in range(len(mat)):
            count=0
            for col in range(len(mat[0])):
                if mat[row][col]==1:
                    count+=1
            if count in d:
                d[count].append(row)
            else:
                d[count]=[row]
        f_keys=sorted(list(d.keys()))
        res=[]
        for row in f_keys:
            res.extend(d[row])
        return res[:k]
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: List[int]
        """
        