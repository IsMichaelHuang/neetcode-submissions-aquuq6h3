class Solution:
    def isPalindrome(self, s: str) -> bool:
        # There is only always going to be 27 letters at one time
        alpha = collections.defaultdict(int)
        letters = "abcdefghijklmnopqrstuvwxyz0123456789"

        s = "".join(ch.lower() for ch in s if ch.isalnum())
        is_odd = len(s) % 2

        middle = 0
        if is_odd:
            middle = len(s) // 2

        for ch in s:
            match ch:
                case _ if ch in letters and ch not in alpha:
                    alpha[ch] += 1
                case _ if ch in alpha and alpha[ch] > 0:
                    alpha[ch] -= 1
                case _ if ch in alpha and alpha[ch] == 0:
                    alpha[ch] += 1
                case _:
                    pass

        remainder = sum(alpha.values())
        print(alpha)
        if is_odd and alpha[s[middle].lower()] <= 0:
            return False

        return not (remainder ^ is_odd)

            

        