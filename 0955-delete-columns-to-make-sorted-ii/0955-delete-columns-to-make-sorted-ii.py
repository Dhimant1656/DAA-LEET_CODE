class Solution(object):
    def minDeletionSize(self, strs):
        n = len(strs)
        m = len(strs[0])
        sorted_pairs = [False] * (n - 1)
        deletions = 0

        for c in range(m):
            for r in range(n - 1):
                if not sorted_pairs[r] and strs[r][c] > strs[r + 1][c]:
                    deletions += 1
                    break
            else:
                for r in range(n - 1):
                    if strs[r][c] < strs[r + 1][c]:
                        sorted_pairs[r] = True

        return deletions