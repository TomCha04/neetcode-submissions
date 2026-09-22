# Definition for a binary tree node. self = the node itself, val = value of that node
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Frame this as a references/pointers problem, not an array/indices one
# Implement Depth-first search through postorder traversal

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def postorder_depth(node):
            depth = 0
            if node is None: return depth
            left_child = postorder_depth(node.left)
            right_child = postorder_depth(node.right)
            return depth + max(left_child, right_child) + 1
        return postorder_depth(root)
