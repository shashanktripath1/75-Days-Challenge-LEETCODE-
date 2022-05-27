class Solution:
    def numberOfSteps(self, num: int) -> int:
        bin_num = str(bin(num))[2:]
        return bin_num.count('1') * 2 + bin_num.count('0') - 1