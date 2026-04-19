class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0

        for num in nums:
            if num -1 not in num_set:
                current = num
                length = 1

                while current + 1 in num_set:
                    length += 1
                    current += 1
                longest = max(longest, length)
        return longest








# num_set = {0,3,2,5,4,6,1,1}





# class Solution:
#     def longestConsecutive(self, nums: List[int]) -> int:
#         num_set = set(nums)
#         longest = 0
        
#         for num in nums:
#             if num - 1 not in num_set:
#                 length = 1
#                 while num + length in num_set:
#                     length += 1
#                 longest = max(length, longest)
            
#         return longest

