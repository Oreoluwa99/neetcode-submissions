class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        max_length = 0
        char_set = set() # allows for O(1) lookup

        for r in range(len(s)):
            while s[r] in char_set:
                char_set.remove(s[l])
                l += 1
            char_set.add(s[r])
            max_length = max(max_length, r-l+1)
        return max_length

# The space complexity is O(n) because we store the characters 
# from the input string s in the char_set and in the worst case, 
# where all characters are unique the set can grow
# up to n elements where n = len(s)