# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        if not root:
            return 0
        return self.paths(root, sum) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)

    def paths(self, root:TreeNode, sum: int) -> int:
        if not root:
            return 0
        res = 0
        if root.val == sum:
            res = res + 1
        res = res + self.paths(root.left, sum - root.val)
        res = res + self.paths(root.right, sum - root.val)

        return res