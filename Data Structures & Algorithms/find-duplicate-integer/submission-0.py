class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        fast = nums[nums[0]] 
        slow = nums[0] 

        while fast != slow:
            slow = nums[slow]
            fast = nums[nums[fast]]

        start = 0 
        while start != slow:
            slow = nums[slow]
            start = nums[start]
        return slow