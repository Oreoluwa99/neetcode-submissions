class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for s in strs:
            cnt = [0] * 26 # 26 empty characters
            for ch in s:
                cnt[ord(ch) - ord("a")] += 1

            res[tuple(cnt)].append(s)
        return list(res.values())