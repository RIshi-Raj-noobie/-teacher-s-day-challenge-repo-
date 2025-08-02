class Solution:
    def maxSubArray(self, nums):
        max_sum = current_sum = nums[0]

        for num in nums[1:]:
            current_sum = max(num, current_sum + num)  # Decide whether to start new subarray or extend current
            max_sum = max(max_sum, current_sum)  # Update global maximum

        return max_sum