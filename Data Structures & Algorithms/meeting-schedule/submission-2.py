"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool: 
        # Edge Case: One or none in interval list; return True
        if len(intervals) <= 1: return True

        intervals.sort(key=lambda x: x.start)

        end = intervals[0].end
        for i in range(1, len(intervals)):
            cur_start = intervals[i].start

            if end > cur_start:
                return False 

            end = intervals[i].end
        return True


