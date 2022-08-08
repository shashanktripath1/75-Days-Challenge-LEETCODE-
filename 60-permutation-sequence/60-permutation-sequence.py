import math
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        arr=[str(i) for i in range(1,n+1)]
        ans=[]
        factorial=math.factorial(n)
        index=k-1
        
        while(arr):
            factorial=factorial//len(arr)
            pos=index//factorial
            number=arr.pop(pos)
            ans.append(number)
            index=index%factorial
        return "".join(ans)