class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_sum = 0
        best = nums[0]

        for num in nums:
            if curr_sum < 0:
                curr_sum = 0
            curr_sum += num
            best = max(best, curr_sum)
        return best
