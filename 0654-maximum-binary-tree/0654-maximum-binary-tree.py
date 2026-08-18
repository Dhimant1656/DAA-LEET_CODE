class Solution:
    def constructMaximumBinaryTree(self, nums):
        if not nums:
            return None

        max_value = max(nums)
        max_index = nums.index(max_value)

        root = TreeNode(max_value)

        root.left = self.constructMaximumBinaryTree(
            nums[:max_index]
        )

        root.right = self.constructMaximumBinaryTree(
            nums[max_index + 1:]
        )

        return root