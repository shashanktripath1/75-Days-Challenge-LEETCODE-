class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:

        # Initialize every variable
        # with first value of array.
        array_sum = 0
        curr_max = -math.inf
        max_so_far = -math.inf
        curr_min = math.inf
        min_so_far = math.inf

        # Concept of Kadane's Algorithm
        for i in range(len(nums)):
            
            # Compute sum of complete array
            array_sum += nums[i]

            # Kadane's Algorithm to find Maximum subarray sum.
            curr_max = max(curr_max + nums[i], nums[i])
            max_so_far = max(max_so_far, curr_max)

            # Kadane's Algorithm to find Minimum subarray sum.
            curr_min = min(curr_min + nums[i], nums[i])
            min_so_far = min(min_so_far, curr_min)
        
        # if the minimum so far is the array sum, then all values are negative
        # then just return the answer of Kadane's algorithm: the highest value
        if (min_so_far == array_sum):
            return max_so_far

        # returning the maximum value 
        # of Kadane's algo on the subarray: max_so_far
        # of the wraparound maximum sum = arr_sum - min_so_far
        return max(max_so_far, array_sum - min_so_far)
