class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        def find_height(root, parent, value, height):
            if not root:
                return 0
            elif root.val == value:
                return (height, parent)
            
            parent = root.val
            left = find_height(root.left, parent, value, height+1)
            if left:
                return left
            
            parent = root.val
            right = find_height(root.right, parent, value, height+1)
            if right:
                return right
        
        if root.val == x or root.val == y: 
            return False
        
        x_height, x_parent = find_height(root, -1, x, 0)
        
        y_height, y_parent = find_height(root, -1, y, 0)
        
        
        if x_parent != y_parent and x_height == y_height:
            return True
        
        return False
