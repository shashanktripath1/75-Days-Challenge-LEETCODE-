class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        unpair={}
        changed.sort(reverse=True)
        original=[]
        for ele in changed:
            if ele*2 in unpair and unpair[ele*2]>0:
                unpair[ele*2]-=1
                original.append(ele)
            elif ele in unpair:
                unpair[ele]+=1
            else:
                unpair[ele]=1
        for val in unpair.values():
            if val!=0:
                return []
        return original
