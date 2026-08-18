class Solution:
    def construct(self, grid):
        def build(row, col, size):
            if size == 1:
                return Node(grid[row][col], True)

            half = size // 2

            topLeft = build(row, col, half)
            topRight = build(row, col + half, half)
            bottomLeft = build(row + half, col, half)
            bottomRight = build(row + half, col + half, half)

            if (
                topLeft.isLeaf
                and topRight.isLeaf
                and bottomLeft.isLeaf
                and bottomRight.isLeaf
                and topLeft.val == topRight.val
                and topLeft.val == bottomLeft.val
                and topLeft.val == bottomRight.val
            ):
                return Node(topLeft.val, True)

            return Node(
                0,
                False,
                topLeft,
                topRight,
                bottomLeft,
                bottomRight
            )

        return build(0, 0, len(grid))