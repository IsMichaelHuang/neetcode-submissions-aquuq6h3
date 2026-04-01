class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        count = {}
        for i in range(len(s)):
            count[s[i]] = i
        
        size, end = 0, 0
        res = []
        for i in range(len(s)):
            end = max(end, count[s[i]])
            size += 1

            if i == end:
                res.append(size)
                size = 0
        
        return res
        