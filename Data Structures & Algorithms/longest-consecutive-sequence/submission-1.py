class Solution:
    # def longestConsecutive(self, nums: List[int]) -> int:
    #     if not nums: # the first edge case
    #         return 0
        
    #     # convert everything to a set
    #     num_set = set(nums) 
    #     longest = 0

    #     for num in num_set:
    #         if num-1 not in num_set:
    #             length = 1
    #             y = num + 1

    #             while y in num_set:
    #                 length += 1
    #                 y += 1
    #             longest = max(longest, length)
    #     return longest

    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        num_set = set(nums)
        longest = 0
        for num in num_set:
            if num-1 not in num_set:
                length = 1
                y = num+1

                while y in num_set:
                    length += 1
                    y += 1
                longest = max(longest, length)
        return longest