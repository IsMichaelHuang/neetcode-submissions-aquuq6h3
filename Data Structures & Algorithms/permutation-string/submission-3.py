class Solution:
    # Both strings are lowercase
    # Both s1/s2 could be length of 1
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1c, s2c = [0] * 26, [0] * 26
        len_s1, len_s2 = len(s1), len(s2)
        match = 0

        if len(s1) > len(s2):
            return False

        for i in range(len_s1):
            s1c[ord(s1[i]) - ord('a')] += 1
            s2c[ord(s2[i]) - ord('a')] += 1
        
        for i in range(26):
            match += (1 if s1c[i] == s2c[i] else 0)
        
        l = 0
        for r in range(len(s1), len(s2)): 
            if match == 26: return True

            index = ord(s2[r]) - ord('a')
            s2c[index] += 1
            if s1c[index] == s2c[index]:
                match += 1
            elif s1c[index] + 1 == s2c[index]:
                match -= 1
            
            index = ord(s2[l]) - ord('a')
            s2c[index] -= 1
            if s1c[index] == s2c[index]:
                match += 1
            elif s1c[index] - 1 == s2c[index]:
                match -= 1
            l += 1
        return match == 26
        
        