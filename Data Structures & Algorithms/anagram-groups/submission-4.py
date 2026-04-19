class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for s in strs:
            key = ''.join(sorted(s)) # this sorts the string alphabetically to give us the key
            anagrams[key].append(s) # this groups all the values of keys together

        return list(anagrams.values())

# The time complexity here is O(n * mlogm)
# The space complexity here is O(m*n) 































# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         anagrams = defaultdict(list)

#         for s in strs:
#             key = ''.join(sorted(s))
#             anagrams[key].append(s)
#         return list(anagrams.values())


# # The time complexity here is O(n * mlogm)
# # The space complexity here is O(m*n) 