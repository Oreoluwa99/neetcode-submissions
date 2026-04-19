class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        l,r = 0, len(heights)-1 # two pointers

        for height in heights:
            smallest_height = min(heights[r], heights[l])
            breadth_rec = r - l
            area = smallest_height * breadth_rec
            res = max(res, area)

            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
            
        return res
