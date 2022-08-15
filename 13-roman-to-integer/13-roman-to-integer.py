class Solution:
    def romanToInt(self, s: str) -> int:
        d={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        prev='I'
        result=0
        for cur in s[::-1]:
            if d[cur]<d[prev]:
                result=result-d[cur]
            else :
                result=result+d[cur]
                prev=cur
        return result
                
                
                
        