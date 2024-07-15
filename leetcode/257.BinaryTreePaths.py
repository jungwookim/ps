from typing import Optional, List

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# 처음 푼 솔루션    
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        result = []
        def backtrack(node, path):
            if node.left is None and node.right is None:
                result.append(path)
                return
            if node.left:
                backtrack(node.left, path + f"->{node.left.val}")
            if node.right:
                backtrack(node.right, path + f"->{node.right.val}")
        backtrack(root, str(root.val))
        return result

# 조금 다듬은 솔루션
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root:
            return []
        result = []
        def dfs(node, path):
            if node:
                path += str(node.val)
                if node.left is None and node.right is None:
                    result.append(path)
                else:
                    path += "->"
                    dfs(node.left, path)
                    dfs(node.right, path)

        dfs(root, "")
        return result
