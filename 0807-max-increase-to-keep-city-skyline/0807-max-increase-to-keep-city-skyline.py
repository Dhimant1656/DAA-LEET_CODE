class Solution(object):
    def maxIncreaseKeepingSkyline(self, grid):
        row_max = [max(row) for row in grid]
        col_max = [max(col) for col in zip(*grid)]

        total_increase = 0
        for r, row in enumerate(grid):
            r_limit = row_max[r]
            for c, height in enumerate(row):
                limit = r_limit if r_limit < col_max[c] else col_max[c]
                total_increase += limit - height

        return total_increase