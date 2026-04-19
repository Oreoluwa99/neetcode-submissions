class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_sum = 0
        best = nums[0]

        for num in nums:
            if curr_sum < 0:
                # Because if your sum so far is negative, 
                # adding it to the next number will only make things worse.
                curr_sum = 0 
            curr_sum += num
            best = max(curr_sum, best)
        return best