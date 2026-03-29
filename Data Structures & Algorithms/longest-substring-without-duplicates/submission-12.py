class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        x = 0
        max_len = []

        for i in range(len(s)):
            while s[i] in max_len:
                max_len.pop(0)
                x = max(x, len(max_len))
            max_len.append(s[i])
            x = max(x, len(max_len))
        return max(x, len(max_len))

        