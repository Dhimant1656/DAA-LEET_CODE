class Solution:
    def constructFromPrePost(self, preorder, postorder):
        pos_map = {value: i for i, value in enumerate(postorder)}

        def helper(pre_start, pre_end, post_start, post_end):
            if pre_start > pre_end:
                return None

            root = TreeNode(preorder[pre_start])

            if pre_start == pre_end:
                return root

            # The next preorder element is the left subtree root
            left_root = preorder[pre_start + 1]

            # Find left subtree root in postorder
            idx = pos_map[left_root]

            # Number of nodes in left subtree
            left_size = idx - post_start + 1

            # Build left subtree
            root.left = helper(
                pre_start + 1,
                pre_start + left_size,
                post_start,
                idx
            )

            # Build right subtree
            root.right = helper(
                pre_start + left_size + 1,
                pre_end,
                idx + 1,
                post_end - 1
            )

            return root

        return helper(
            0,
            len(preorder) - 1,
            0,
            len(postorder) - 1
        )