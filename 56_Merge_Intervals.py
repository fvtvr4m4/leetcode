class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        merged = []
        intervals.sort(key=lambda interval: interval[0])
        for i in range(0, len(intervals)):
            if len(merged) == 0:
                merged.append(intervals[i])
            else:
                lower_interval = merged.pop()
                upper_interval = intervals[i]
                if lower_interval[1] >= upper_interval[0]:
                    end = max(lower_interval[1], upper_interval[1])
                    merged_interval = (lower_interval[0], end)
                    merged.append(merged_interval)
                else:
                    merged.append(lower_interval)
                    merged.append(upper_interval)
        return merged
