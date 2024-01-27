from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals = sorted(intervals, key=lambda x: x[0])
        result_intervals = []
        extendee = intervals[0]

        for interval in intervals[1:]:
            if interval[0] <= extendee[1]:
                extendee[1] = max(extendee[1], interval[1])
            else:
                result_intervals.append(extendee)
                extendee = interval

        result_intervals.append(extendee)
        return result_intervals
