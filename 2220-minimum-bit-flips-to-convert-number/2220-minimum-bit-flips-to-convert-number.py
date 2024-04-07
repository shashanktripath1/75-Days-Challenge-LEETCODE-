class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        xor_result = start ^ goal
        flips = 0
        while xor_result:
            flips += xor_result & 1
            xor_result >>= 1
        return flips