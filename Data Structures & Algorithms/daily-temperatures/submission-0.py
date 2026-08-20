class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        output = [0 for _ in range(len(temperatures))]
        for i in range(len(temperatures)-1,-1,-1):
            if not stack:
                output[i] = 0
                stack.append([temperatures[i],i])
                continue 
            while stack and stack[-1][0] <= temperatures[i]:
                stack.pop()
            if stack:
                output[i] = stack[-1][1] - i
                stack.append([temperatures[i],i])
                continue
            else:
                output[i] = 0
                stack.append([temperatures[i],i])
                continue 
        return output