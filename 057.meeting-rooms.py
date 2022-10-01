from typing import (
    List,
)

from pandas import Interval


"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""


class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: if a person could attend all meetings
    """
    def can_attend_meetings(self, intervals: List[Interval]) -> bool:
        busy = set()
        for interval in intervals:
            meeting_start, meeting_end = interval.start, interval.end
            for i in range(meeting_start, meeting_end + 1):
                if i in busy:
                    return False
                else:
                    busy.add(i)
        return True


sol = Solution().can_attend_meetings(
    [(0,30), (5, 10), (15, 20)])
print(sol)
