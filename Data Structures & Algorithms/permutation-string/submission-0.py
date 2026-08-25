from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        cs1 = Counter(s1)
        cs2 = Counter(s2[:len(s1)])

        left = 0
        right = len(s1)-1 

        while right < len(s2):
            if cs1 == cs2:
                return True
            right +=1
            
            if right == len(s2):
                break 
            cs2[s2[left]] -= 1
            if cs2[s2[left]] == 0:
                del cs2[s2[left]]
            
            left += 1
            cs2[s2[right]] += 1 
        return False
        