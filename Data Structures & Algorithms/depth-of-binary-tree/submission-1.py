# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution: # Attempt 2
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def post_order(node):
            if node == None: return 0
            left = post_order(node.left) # left subtree's depth
            right = post_order(node.right) # right subtree's depth
            return max(left, right) + 1
        return post_order(root)
