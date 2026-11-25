from collections import Counter

class Solution(object):
    def canReorderDoubled(self, arr):
        counts = Counter(arr)

        for x in sorted(counts, key=abs):
            need = counts[x]
            if need > 0:
                if counts[2 * x] < need:
                    return False
                counts[2 * x] -= need

        return True