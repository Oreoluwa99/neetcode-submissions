class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # check if any value appears more than twice
        # let's say we use a two pointer..

        # make a dictionary. if any number has value of 2, it does appear twice

        # nums.sort()

        # for i in range(1, len(nums)):
        #     if nums[i] == nums[i-1]:
        #         return True
        # return False

        seen = set()

        for i in nums:
            if i in seen:
                return True
            else:
                seen.add(i)
        return False