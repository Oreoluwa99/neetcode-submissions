class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0] # the first string is the prefix there

        for s in strs[1:]:
            while not s.startswith(prefix):
                prefix = prefix[:-1] # remove the last character

                if not prefix: # if nothing left
                    return '' # no common prefix at all
        return prefix