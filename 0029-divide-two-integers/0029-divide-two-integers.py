class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == -2147483648 and divisor == 1:
            return -2147483648
        elif dividend == 2147483647 and divisor == -1:
            return -2147483647
        elif dividend == 2147483647 and divisor == 1:
            return 2147483647
        elif dividend == -2147483648 and divisor == -1:
            return 2147483647
        
        divisor1 = abs(divisor)
        dividend1 = abs(dividend)
        count = 0
        
        while divisor1 <= dividend1:
            x = 0
            while dividend1 >= divisor1 << x:
                x += 1
            count += 1 << (x - 1)
            dividend1 -= divisor1 << (x - 1)
        
        if count >= 2147483647:
            return 2147483647
        elif divisor < 0 and dividend < 0:
            return count
        elif divisor < 0 or dividend < 0:
            count = -count
        return count

