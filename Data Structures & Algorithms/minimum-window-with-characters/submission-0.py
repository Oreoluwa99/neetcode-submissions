class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t:
            return ""
        
        # Count required chars (Counter handles duplicates)
        countT = Counter(t)
        window = {}

        have, need = 0, len(countT)     # number of satisfied keys vs total distinct keys
        res = [-1, -1]
        reslen = float("inf")
        l = 0

        for r in range(len(s)):
            # expand window to include s[r]
            window[s[r]] = 1 + window.get(s[r], 0)

            # if this char's count just reached what we need, we satisfied one key
            if s[r] in countT and window[s[r]] == countT[s[r]]:
                have += 1
            
            # shrink while valid
            while have == need:
                # update best window (NOTE: store [l, r], not [r, l])
                if (r - l + 1) < reslen:
                    res = [l, r]
                    reslen = r - l + 1

                # pop from the left
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1

        # return result
        l, r = res
        return s[l:r+1] if reslen != float("inf") else ""
