class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0] # the prefix

        for s in strs[1:]: # loop through all the string in s
            while not s.startswith(prefix):
                prefix = prefix[:-1]

                if not prefix:
                    return ""
        return prefix





























# class Solution:
#     def longestCommonPrefix(self, strs: List[str]) -> str:
#         prefix = strs[0]   # start with the first word as the initial prefix

#         for s in strs[1:]:   # compare with every other string
#             while not s.startswith(prefix):  # shrink prefix until it matches
#                 prefix = prefix[:-1]         # remove last char
#                 if not prefix:
#                     return ""                # no common prefix left

#         return prefix


