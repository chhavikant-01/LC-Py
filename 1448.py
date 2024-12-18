# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        if not root:
            return 0
        
        # Stack will store tuples of (node, max_so_far)
        stack = [(root, float('-inf'))]
        good_count = 0
        
        while stack:
            node, max_so_far = stack.pop()
            
            # If current node value >= max_so_far, it's a good node
            if node.val >= max_so_far:
                good_count += 1
            
            # Update max_so_far for children
            new_max = max(max_so_far, node.val)
            
            # Add children to stack
            if node.right:
                stack.append((node.right, new_max))
            if node.left:
                stack.append((node.left, new_max))
        
        return good_count
        
