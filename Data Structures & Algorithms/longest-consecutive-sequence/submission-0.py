class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # check if the list is empty
        if not nums:
            return 0
        
        nums_set = set(nums) # convert everything to a set and remove duplicates
        longest = 0

        for num in nums_set:
            if (num-1) not in nums_set:
                length = 1
                next_num = num + 1
                
                while next_num in nums_set:
                    length += 1
                    next_num += 1
                longest = max(length, longest)
        return longest