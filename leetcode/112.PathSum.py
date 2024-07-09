from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        sums = []
        def dfs(node, acc):
            # if leaf
            if node.left is None and node.right is None:
                sums.append(acc)
                return
            if node.left:
                dfs(node.left, acc + node.left.val)
            if node.right:
                dfs(node.right, acc + node.right.val)

        dfs(root, root.val)
        return targetSum in sums