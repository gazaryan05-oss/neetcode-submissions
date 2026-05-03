class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            m = (left + right) // 2

            if nums[m] > nums[right]:
                left = m + 1
            else:
                right = m
        
        min_i = right

        if  min_i == 0:
            l, r = 0, len(nums) - 1
        elif target >= nums[0] and target <= nums[min_i - 1]:
            l, r = 0, min_i - 1
        else:
            l,r = min_i, len(nums) - 1

        while l <= r:
            m = (l + r) // 2

            if target > nums[m]:
                l = m + 1
            elif target < nums[m]:
                r = m - 1
            else:
                return m
        return -1