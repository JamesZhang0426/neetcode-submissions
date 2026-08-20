class Solution:
    def trap(self, height: List[int]) -> int:
        maxleft = []
        lastmaxleft = 0
        maxright = []
        lastmaxright = 0
        total = 0
        for i in range(len(height)):
            maxleft.append(lastmaxleft)
            if height[i] > maxleft[-1]:
                lastmaxleft = height[i]
        for j in range(len(height) - 1, -1, -1):
            maxright.append(lastmaxright)
            if height[j] > maxright[-1]:
                lastmaxright = height[j]
        maxright.reverse()
        for k in range(len(height)):
            this_cell = min(maxright[k], maxleft[k]) - height[k]
            if this_cell > 0:
                total += this_cell
        return total
