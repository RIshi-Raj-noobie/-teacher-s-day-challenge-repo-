class Solution:
    def merge(self, intervals):
        if not intervals:
            return []

        # Sort intervals based on start time
        intervals.sort(key=lambda x: x[0])

        merged = [intervals[0]]

        for current in intervals[1:]:
            last = merged[-1]
            # If current interval overlaps with the last merged interval
            if current[0] <= last[1]:
                # Merge them by updating the end time
                last[1] = max(last[1], current[1])
            else:
                merged.append(current)

        return merged