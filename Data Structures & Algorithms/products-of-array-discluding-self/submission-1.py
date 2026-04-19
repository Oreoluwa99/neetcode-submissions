class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        n = len(nums)
        l_arr, r_arr = ([0]*n), ([0]*n)
        l_mult, r_mult = 1, 1
        for i in range(n):
            j = -1 - i
            l_arr[i],  r_arr[j]= l_mult, r_mult
            l_mult = nums[i] * l_mult
            r_mult = nums[j] * r_mult
        return [(l * r) for l, r in zip(l_arr, r_arr)]
