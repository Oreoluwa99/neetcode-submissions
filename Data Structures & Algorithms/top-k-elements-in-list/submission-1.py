class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
            freq = Counter(nums)
            buckets = [[] for _ in range(len(nums) + 1)]
            
            # put each number in its frequency bucket
            for val, f in freq.items():
                buckets[f].append(val)
            
            ans = []
            # go backwards from high frequency to low
            for f in range(len(nums), 0, -1):
                for val in buckets[f]:
                    ans.append(val)
                    if len(ans) == k:
                        return ans
