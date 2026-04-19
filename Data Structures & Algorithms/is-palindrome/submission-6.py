class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1
        while l < r:
            #if the current character is not a letter or number, skip it
            while l < r and not s[l].isalnum(): 
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True


# The time complexity for this is O(n) where n is the number of elements in the array
# At each iteration, either l moves right or r moves left
# They may look nested, but they are not since they don't restart for every character 
# They just keep advancing pointers
# Since we don't use recursion, no stack, no new list or string, this is an O(1) operation
