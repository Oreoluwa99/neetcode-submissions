class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        countS, countT = {}, {}
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        return countS == countT
# The time complexity is O(n+m) where n 
# is the length of string n and m is the length of string m
# The space complexity is O(1) since in the worst case, we will have 26 characters 
# which is O(26) -- O(1)

# Time complexity is O(n + m) 
# Space complexity is O(26) which is proportional to O(1)





























# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         if len(s) != len(t):
#             return False
        
#         countS, countT = {}, {}
#         for i in range(len(s)):
#             countS[s[i]] = countS.get(s[i], 0) + 1
#             countT[t[i]] = countT.get(t[i], 0) + 1
#         return countS == countT
        