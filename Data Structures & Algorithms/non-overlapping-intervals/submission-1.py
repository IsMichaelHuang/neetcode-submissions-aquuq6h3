class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        sIntervals = sorted(intervals, key=lambda x: x[0])

        res = 0
        prevEnd = sIntervals[0][1]
        for s, e in sIntervals[1:]:
            if s >= prevEnd:
                prevEnd = e
            else:
                res += 1
                prevEnd = min(prevEnd, e)

        return res

