# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        # Handle empty tree case
        if not root:
            return 0
        
        # Initialize queue with root node and its level
        queue = [(root, 1)]
        max_depth = 0
        
        # Process nodes level by level
        while queue:
            node, level = queue.pop(0)
            
            # Update max_depth if current level is deeper
            max_depth = max(max_depth, level)
            
            # Add children to queue with incremented level
            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))
        
        return max_depth
        
