class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        n = bin(n)
        for i in n:
            if i == '1':
                res += 1
        return res
        