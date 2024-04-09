class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        lsum = sum(cardPoints[:k])  # Initialize left sum
        rsum = 0
        sum_ = lsum
        
        j = len(cardPoints) - 1
        
        for i in range(k - 1, -1, -1):
            lsum -= cardPoints[i]
            rsum += cardPoints[j]
            j -= 1

            sum_ = max(sum_, lsum + rsum)
        
        return sum_
