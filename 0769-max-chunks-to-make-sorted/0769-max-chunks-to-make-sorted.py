class Solution(object):
    def maxChunksToSorted(self, arr):
        chunks = 0
        max_seen = 0

        for i, val in enumerate(arr):
            if val > max_seen:
                max_seen = val

            if max_seen == i:
                chunks += 1

        return chunks