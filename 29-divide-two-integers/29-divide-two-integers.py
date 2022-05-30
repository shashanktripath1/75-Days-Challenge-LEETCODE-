class Solution:
    def divide(self, dividend: int, divisor: int) -> int:

        s = str(eval(str(dividend)+ "/" +str(divisor))) #divison complete
        return min(int(s[:s.index(".")]), 2**31-1)   