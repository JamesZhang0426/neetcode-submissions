class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1

        while left<right:
            mid = (left+right)//2

            if nums[right] < nums[mid]:
                left = mid + 1 
            else:
                right = mid 

        minimum = left 

        if nums[minimum] <= target <= nums[-1]:
            right = len(nums)-1
            left = minimum 
        else:
            right = minimum
            left = 0

        while left <= right:
            mid = (left+right)//2

            if nums[mid]  == target:
                return mid 

            elif nums[mid] < target:
                left = mid + 1 
            else:
                right = mid -1       

        return -1 