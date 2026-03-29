class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        cc = collections.defaultdict(int)
        l = 0
        res = 0
        max_freq = 0

        for r, ch in enumerate(s):
            cc[ch] += 1

            # Always keep track of the most common
            max_freq = max(max_freq, cc[ch])
            # The + 1 is to make this math inclusive
            if (r - l + 1) - max_freq > k:
                # Move left pointer
                cc[s[l]] -= 1
                l += 1
            
            # r - l + 1 is the window
            res = max(res, (r - l + 1))
        return res

        