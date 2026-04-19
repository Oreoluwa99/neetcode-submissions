class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for num in range(1, len(nums)):
            if nums[num] == nums[num-1]:
                return True
        return False

# This is an O(nlogn) time complexity since sorting has a time complexity of O(n log n) and
# since we are going through all the elements in the array, this is another O(n) operation,
# So the total is O(nlogn + n) which is O(nlogn)is the time complexity
# And for the space complexity, we do not create a new memory, so it is O(1)