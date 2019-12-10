# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        else:
            right_depth = self.maxDepth(root.right)
            left_depth = self.maxDepth(root.left)
        return max(right_depth, left_depth) + 1