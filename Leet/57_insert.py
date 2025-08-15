class Solution:
    def insert(self, intervals, newInterval):
        # Approach (notes):
        # 1) Add all intervals that end before newInterval starts (no overlap).
        # 2) Merge all intervals that overlap with newInterval by expanding its [start,end].
        # 3) Append the merged newInterval, then append the rest.
        # Time: O(n), Space: O(n)
        res = []
        i, n = 0, len(intervals)
        s, e = newInterval

        # 1) intervals completely before newInterval
        while i < n and intervals[i][1] < s:
            res.append(intervals[i])
            i += 1

        # 2) merge overlaps with newInterval
        while i < n and intervals[i][0] <= e:
            s = min(s, intervals[i][0])
            e = max(e, intervals[i][1])
            i += 1
        res.append([s, e])

        # 3) remaining intervals
        while i < n:
            res.append(intervals[i])
            i += 1

        return res
