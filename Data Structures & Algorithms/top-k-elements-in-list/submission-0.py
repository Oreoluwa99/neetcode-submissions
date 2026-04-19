class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums) # count how often each number appears

        #store them in buckets
        buckets = [[] for _ in range(len(nums) + 1)]

        # store each number in their frequency bucket
        for key, val in freq.items():
            buckets[val].append(key)
        
        ans = []

        # go backwards from the highest frequency
        for i in range(len(nums), 0, -1):
            for val in buckets[i]:
                ans.append(val)
                if len(ans) == k:
                    return ans