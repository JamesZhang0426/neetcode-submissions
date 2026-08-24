class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        letters = set()

        longest_count = 1
        letters.add(s[0])

        left = 0
        right = 1 

        while right < len(s):

            if s[right] not in letters:
                letters.add(s[right])
                longest_count = max(right - left + 1,longest_count)
                right += 1

            else:
                letters.remove(s[left])
                left += 1

        return longest_count


            