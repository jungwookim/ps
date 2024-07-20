# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_diameter = 0
    
        def depth(node):
            nonlocal max_diameter
            if not node:
                return 0
            left_depth = depth(node.left)
            right_depth = depth(node.right)
            # 현재 노드에서의 지름을 계산
            max_diameter = max(max_diameter, left_depth + right_depth)
            # 현재 노드의 깊이를 반환
            return 1 + max(left_depth, right_depth)
        
        depth(root)
        return max_diameter