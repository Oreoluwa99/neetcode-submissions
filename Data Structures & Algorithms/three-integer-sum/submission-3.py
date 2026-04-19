class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        res = []

        for i in range(n-2): # since we are using 3 numbers
            if i > 0 and nums[i] == nums[i-1]: # skip duplicates
                continue
            
            # since i is already fixed in the outer loop
            l, r = i+1, n-1

            while l<r:
                threeSum = nums[i] + nums[l] + nums[r]
                if threeSum == 0:
                    res.append([nums[i], nums[l], nums[r]])

                    # move l and r and skip duplicates
                    l += 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                    r -= 1
                    while l < r and nums[r] == nums[r+1]:
                        r -= 1

                elif threeSum < 0:
                    l += 1
                else:
                    r -= 1
        return res