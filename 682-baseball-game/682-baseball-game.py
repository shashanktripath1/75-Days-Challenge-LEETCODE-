class Solution:
    def calPoints(self, ops: List[str]) -> int:
        l=[]
        for i in ops:
            if i.isdigit():
                l.append(int(i))
            elif i=='C':
                l.pop()
            elif i=='D':
                l.append(l[-1]*2)
            elif i=='+':
                l.append(l[-1]+l[-2])
            else:
                l.append(int(i))
        return sum(l)
                
                
        