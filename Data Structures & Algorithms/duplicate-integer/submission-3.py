class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # sort the values
        # if in in range (1, len(nums)), and the previous number = current number, return True
        # else return False

        # nums.sort()
        # for i in range(1, len(nums)): # start at the second number after the first number
        #     if nums[i] == nums[i-1]:
        #         return True
        # return False

        seen = set()

        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False