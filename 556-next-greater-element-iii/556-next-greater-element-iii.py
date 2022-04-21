class Solution:
    def nextGreaterElement(self, n: int) -> int:
        digits=list(str(n))
        i=j=len(digits)-1
        while i and digits[i]<=digits[i-1]:
            i-=1
        if i==0:
            return -1
        while digits[j]<=digits[i-1]:
            j-=1
        digits[j],digits[i-1]=digits[i-1],digits[j]
        digits[i:]=digits[i:][::-1]
        res="".join(digits)
        return res if int(res)<2**31 else -1
        