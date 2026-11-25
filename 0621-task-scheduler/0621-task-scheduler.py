from collections import Counter

class Solution(object):
    def leastInterval(self, tasks, n):
        counts = Counter(tasks).values()
        max_freq = max(counts)
        max_count = list(counts).count(max_freq)

        intervals = (max_freq - 1) * (n + 1) + max_count
        return max(len(tasks), intervals)