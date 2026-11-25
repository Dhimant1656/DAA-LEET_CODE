class Solution(object):
    def matrixScore(self, grid):
        m = len(grid)
        n = len(grid[0])

        # Every row's first bit becomes 1
        score = m * (1 << (n - 1))

        for c in range(1, n):
            ones = sum(grid[r][c] == grid[r][0] for r in range(m))
            max_ones = ones if ones > m - ones else m - ones
            score += max_ones * (1 << (n - 1 - c))

        return score