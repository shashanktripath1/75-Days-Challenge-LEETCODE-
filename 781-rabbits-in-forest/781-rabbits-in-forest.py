import math
class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        d={}
        ans=0
        for i in answers:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        for key,value in d.items():
            if key+1<value:
                ans+=(key+1)*math.ceil(value/(key+1))
            else:
                ans+=key+1
        return ans