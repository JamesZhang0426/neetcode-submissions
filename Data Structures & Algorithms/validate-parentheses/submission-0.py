class Solution:
    def isValid(self, s: str) -> bool:
        pa = {')':'(','}':'{',']':'['}

        stack = []

        for p in s:
            if p not in pa:
                stack.append(p)
                continue
            
            if p in pa:
                if not stack:
                    return False
                if stack[-1] == pa[p]:
                    stack.pop()
                else:
                    return False
        if stack:
            return False

        return True