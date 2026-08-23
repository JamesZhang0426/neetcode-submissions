class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        maxeat = max(piles)
        mineat = 1
        ans = maxeat
        while mineat <= maxeat:
            
            mid = (maxeat+mineat) // 2

            hours = 0
            for pile in piles:
                hours += math.ceil(pile / mid)

            if hours <= h:
                ans = mid
                maxeat = mid - 1
            else:
                mineat = mid + 1 

        return ans 
