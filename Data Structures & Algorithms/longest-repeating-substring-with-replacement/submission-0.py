class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        max_freq = 0
        best = 0 # stores the longest valid window seen
        count = {} # keeps track of how many times a letter appears in the window

        for r, ch in enumerate(s):
            count[s[r]] = 1 + count.get(s[r], 0)
            max_freq = max(max_freq, count[ch]) # update the most frequent character count

            while ((r-l+1) - max_freq) > k:
                count[s[l]] -= 1 # shrink the window by removing the left most character
                l += 1
            best = max(best, (r-l+1))

        return best 