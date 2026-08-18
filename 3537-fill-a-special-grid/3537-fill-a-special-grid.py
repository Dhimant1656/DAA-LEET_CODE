class Solution:
    def specialGrid(self, n):
        if n == 0:
            return [[0]]

        small = self.specialGrid(n - 1)

        size = len(small)
        grid = [[0] * (size * 2) for _ in range(size * 2)]

        total = size * size

        for i in range(size):
            for j in range(size):
                # Top-right: smallest
                grid[i][j + size] = small[i][j]

                # Bottom-right
                grid[i + size][j + size] = small[i][j] + total

                # Bottom-left
                grid[i + size][j] = small[i][j] + 2 * total

                # Top-left: largest
                grid[i][j] = small[i][j] + 3 * total

        return grid