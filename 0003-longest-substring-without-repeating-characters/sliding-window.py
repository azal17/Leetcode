class Solution:
   def lengthOfLongestSubstring(self, s: str) -> int:
    n = len(s)
    max_val = 0
    char_set = set()
    left = 0

    for right in range(n):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        char_set.add(s[right])
        max_val = max(max_val, right - left + 1)

    return max_val
