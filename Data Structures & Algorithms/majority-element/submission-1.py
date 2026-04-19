class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
            if counts[num] > len(nums)//2:
                return num
# we use a dictionary to track how many times each number appears
# and as soon as a number's count exceeds n/2, we can return it