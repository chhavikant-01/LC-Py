# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        # We'll use a stack to track our state
        # Each element will be: (node, going_right, current_length)
        # going_right indicates the direction we should go next
        # current_length is the length of the zigzag path up to this point
        stack = [(root, True, 0), (root, False, 0)]
        max_length = 0
        
        while stack:
            node, going_right, current_length = stack.pop()
            
            # Update our maximum length seen so far
            max_length = max(max_length, current_length)
            
            if going_right:
                # If we're supposed to go right
                if node.right:
                    # Continue the zigzag path by going right
                    # Next move should be left
                    stack.append((node.right, False, current_length + 1))
                
                # Start a new potential zigzag path going left
                if node.left:
                    stack.append((node.left, True, 1))
                    
            else:
                # If we're supposed to go left
                if node.left:
                    # Continue the zigzag path by going left
                    # Next move should be right
                    stack.append((node.left, True, current_length + 1))
                
                # Start a new potential zigzag path going right
                if node.right:
                    stack.append((node.right, False, 1))
        
        return max_length
        
