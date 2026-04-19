class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights)-1
        res = 0

        for h in heights:
            breadth = r - l
            smallest_height = min(heights[r], heights[l])
            area = smallest_height * breadth
            res = max(res, area)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return res 

