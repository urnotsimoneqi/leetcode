import queue

# Definition for a binary tree node.
 class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return
        q = queue.Queue()
        q.put(root)
        while not q.empty():
            current = q.get()
            temp = current.left
            current.left = current.right
            current.right = temp
            if current.left:
                q.put(current.left)
            if current.right:
                q.put(current.right)
        return root
