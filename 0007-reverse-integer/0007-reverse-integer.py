class Solution:
    def reverse(self, x: int) -> int:
        rev=0
        sign=1
        if x<0:
            x=x*-1
            sign=sign*-1
        while x>0:
            last_digit=x%10
            x=x//10
            rev=(rev*10)+last_digit
        if  not -2147483648<rev<2147483647:
            return 0
        return rev*sign