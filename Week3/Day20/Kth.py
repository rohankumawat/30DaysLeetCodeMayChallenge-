# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        def inorder(root):
            if root is None:
                return []
            inLeft = inorder(root.left)
            root_val = [root.val]
            inRight = inorder(root.right)
            return inLeft + root_val + inRight
        
        return inorder(root)[k-1]
