# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        def constructBST(preorder, start, end):
            if start > end:
                return None
            
            node = TreeNode(preorder[start])

            i = start
            while i <= end:
                if preorder[i] > node.val:
                    break
                i = i + 1

            node.left = constructBST(preorder, start + 1, i - 1)
            node.right = constructBST(preorder, i, end)

            return node
        
        return constructBST(preorder,0,len(preorder) - 1)
