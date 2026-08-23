class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        left = 0
        right = len(nums)-1 

        while left < right:
            mid = (left+right)//2

            if nums[right] < nums[mid]:
                left = mid +1 
            else:
                right = mid  

        return nums[left] 



# 1 2 3 4 5
# 5 1 2 3 4
# 3 4 5 1 2 