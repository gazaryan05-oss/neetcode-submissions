class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        max_count = 0
        for num in nums:
            if num - 1 in seen:
                continue 
            cur = num
            count = 1
            while cur + 1 in seen:
                cur += 1
                count += 1
            max_count = max(max_count, count)
        
        return max_count
        

