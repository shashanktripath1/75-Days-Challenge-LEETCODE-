class Solution:
    def maximum69Number (self, num: int) -> int:
        check=str(num)
        return int(check.replace('6','9',1))
