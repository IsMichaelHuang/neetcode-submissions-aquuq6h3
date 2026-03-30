"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if len(intervals) < 1: return 0

        startTime = sorted([i.start for i in intervals])
        endTime = sorted([i.end for i in intervals])

        res, count = 0, 0
        s, e = 0, 0
        while s < len(intervals):
            # Ending meeting
            if startTime[s] < endTime[e]:
                s += 1
                count += 1
            # Starting meetings
            else:
                e += 1
                count -= 1
            res = max(res, count)
        return res

