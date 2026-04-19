class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Start with two pointers: left (l) and right (r)
        l, r = 0, len(nums) - 1

        # Keep searching while the window is valid
        while l <= r:
            # Find the middle index
            mid = (l + r) // 2

            # Case 1: Check if middle element is the target
            if nums[mid] == target:
                return mid

            # Case 2: Figure out which half is sorted
            if nums[l] <= nums[mid]:
                # Left half [l .. mid] is sorted

                # If the target is NOT inside this sorted left half,
                # then throw away the left side
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1  # search on the right
                else:
                    r = mid - 1  # search inside the left half

            else:
                # Right half [mid .. r] is sorted

                # If the target is NOT inside this sorted right half,
                # then throw away the right side
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1  # search on the left
                else:
                    l = mid + 1  # search inside the right half

        # Target not found
        return -1
