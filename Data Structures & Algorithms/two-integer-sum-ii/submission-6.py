class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while l < r: 
            curr_sum = numbers[l] + numbers[r]

            if curr_sum > target:
                r -= 1
            elif curr_sum < target:
                l += 1
            else:
                return [l+1, r+1]
# The time complexity is O(n) is at the worst case we
# will loop over all of the elements in the array (l and r)
# It is also an O(1) operation because we do not store any 
# other elements in any array or hashmaps or recursion stacks whatsoever