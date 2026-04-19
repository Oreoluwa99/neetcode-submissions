class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        res = 0

        for h in heights:
            breadth = r - l
            height = min(heights[r], heights[l])
            area = breadth * height
            res = max(res, area)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return res


# This is an O(n) solution since the worst thing that could happen is that
# our left and right pointers go through all the elements in the array
# Also, since we are not creating any special array or hastable, this is an O(1) solution