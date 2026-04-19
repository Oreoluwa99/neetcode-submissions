class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])

        l, r = 0, (cols*rows - 1)

        while l <= r:
            m = (r + l) // 2

            # Convert m back to 2D indices
            row, col = m // cols, m % cols

            if target > matrix[row][col]:
                l = m + 1
            elif target < matrix[row][col]:
                r = m -1
            else:
                return True

        return False






# The brute force solution

# class Solution:
#     def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
#         for row in matrix:
#             for value in row:
#                 if value == target:
#                     return True
#         return False