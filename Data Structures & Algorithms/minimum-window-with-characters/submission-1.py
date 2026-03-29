class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count_map, window = {}, {}
        res, res_len = [-1, -1], float('inf')
        
        if len(t) == 0:
            return "" 

        # We need a minimum window of size t first, but this is a dynamic approach
        for ch in t:
            count_map[ch] = count_map.get(ch, 0) + 1 
        have, need = 0, len(count_map)
        

        l = 0
        for r in range(len(s)):
            ch = s[r]
            window[ch] = window.get(ch, 0) + 1

            if ch in count_map and count_map[ch] == window[ch]:
                have += 1 
            
            while have == need:
                if (r - l + 1) < res_len:
                    res_len = (r - l + 1)
                    res = [l, r]
                
                # Did we remove a curcial char?
                window[s[l]] -= 1
                if s[l] in count_map and window[s[l]] < count_map[s[l]]:
                    have -= 1
                l += 1

        return s[res[0]:res[1] + 1] if res_len != float('inf') else ""

        # Time: O(n) where n is the length of the given string "s"
        # Space: O(m) where m is the output of the shortest substring that includes all char in t

        