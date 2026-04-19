class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {} # the hashmap

        for i, n in enumerate(nums): # index and value

            diff = target - n

            if diff in prevMap:
                return [prevMap[diff], i]

            prevMap[n] = i


