
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        all_numbers = set(nums)
        longest = 1
        for num in all_numbers:
            if num - 1 not in all_numbers:
                lenght = 1

                while num+1 in all_numbers:
                    lenght += 1
                    longest = max(longest,lenght)
                    num+=1 

        return longest            
