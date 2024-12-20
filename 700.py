# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        current = root
        
        while current:
            if current.val == val:
                return current  # Return the actual node with its subtree
            
            if val < current.val:
                current = current.left
            else:
                current = current.right
        
        return None  # Return None if value not found
