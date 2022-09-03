class Solution:

    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        res = []

        def backtrack(num):
            if len(str(num)) == n:
                if num not in res:
                    res.append(num)
                return
            check = num % 10
            if (check + k) <= 9:
                num1 = (num * 10) + (check + k)
                backtrack(num1)
            if (check - k) >= 0:
                num2 = (num * 10) + (check - k)
                backtrack(num2)
        for i in range(1, 10):
            backtrack(i)
        return res