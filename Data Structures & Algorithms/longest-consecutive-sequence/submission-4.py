class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        longest = 0

        for num in seen:
            if num - 1 not in seen:  
                leng = 1
                cur = num
                
                while cur + 1 in seen:
                    cur += 1
                    leng += 1
                
                longest = max(leng, longest)
        
        return longest
        