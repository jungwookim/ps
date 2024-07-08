from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        result = float('inf')
        def dfs(node, depth):
            nonlocal result
            if node.left == None and node.right == None:
                result = min(depth, result)
                return
            depth += 1
            if node.left:
                dfs(node.left, depth)
            if node.right:
                dfs(node.right, depth)

        dfs(root, 1)
        return result