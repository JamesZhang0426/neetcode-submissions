from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}

        left = 0
        longest = 0 
        counts = defaultdict(int)

        for right in range(len(s)):
            counts[s[right]] += 1
            maxfreq = max(counts.values())

            while right - left + 1 > maxfreq + k:
                counts[s[left]] -= 1
                left +=1 
                maxfreq = max(counts.values())
        
            longest = max(longest,right - left + 1)

        return longest