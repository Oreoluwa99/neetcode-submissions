class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # sort the values
        # if in in range (1, len(nums)), and the previous number = current number, return True
        # else return False

        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                return True
        return False