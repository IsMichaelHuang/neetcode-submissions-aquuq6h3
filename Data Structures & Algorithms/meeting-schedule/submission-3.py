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
        for node in intervals[1:]:
            cur_start = node.start

            if end > cur_start: return False 

            end = node.end
        return True


