class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list) # create a default value for a key if it doesn't exist

        for s in strs:
            key = ''.join(sorted(s))
            anagrams[key].append(s)
        return list(anagrams.values())

# The time complexity here is O(n * mlogm)
# The space complexity here is O(m*n) 