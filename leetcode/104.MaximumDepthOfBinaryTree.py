from typing import Optional
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        result = -1
        def dfs(node, depth):
            nonlocal result
            if node is None:
                result = max(depth, result)
                return
            if node.left is None and node.right is None:
                result = max(depth, result)
            else:
                depth += 1
                dfs(node.left, depth)
                dfs(node.right, depth)

        dfs(root, 1)
        return result
    

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        result = -1
        def dfs(node, depth):
            nonlocal result
            if node.left is None and node.right is None:
                result = max(depth, result)
                return
            else:
                depth += 1
                if node.left:
                    dfs(node.left, depth)
                if node.right:
                    dfs(node.right, depth)

        dfs(root, 1)
        return result