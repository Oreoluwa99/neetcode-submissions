class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones) # the most negative now is the largest positive

        while len(stones) > 1:
            y = -heapq.heappop(stones) # pop the largest
            x = -heapq.heappop(stones) # pop the second largest
            if y > x:
                heapq.heappush(stones, -(y-x))

        return -stones[0] if stones else 0
        