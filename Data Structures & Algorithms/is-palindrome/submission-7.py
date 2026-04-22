class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1

        while l < r:

            while l<r and not s[l].isalnum(): # if it is not a digit or a letter
                l += 1
            while l<r and not s[r].isalnum(): # if it is not a digit or a letter
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True





























# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         l = 0
#         r = len(s) - 1

#         while l < r:

#             while l < r and not s[l].isalnum(): # skip this character if it's not a letter or digit
#                 l += 1
#             while l < r and not s[r].isalnum(): # skip this character if it's not a letter or digit
#                 r -= 1
#             if s[l].lower() != s[r].lower():
#                 return False
#             l += 1
#             r -=1 
#         return True