class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        flips = 0
        while start > 0 or goal > 0:
            start_bit, goal_bit = start & 1, goal & 1
            if start_bit != goal_bit:
                flips += 1
            start >>= 1
            goal >>= 1
        return flips