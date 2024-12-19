# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        if not root:
            return []
        
        # Initialize queue with root node and level
        queue = deque([(root, 0)])
        right_view = []
        current_level = 0
        
        # Keep track of the rightmost value at each level
        rightmost_value = {}
        
        while queue:
            node, level = queue.popleft()
            
            # Update the rightmost value for this level
            # Since we process left to right, the last value 
            # we see at each level will be the rightmost
            rightmost_value[level] = node.val
            
            # Add children with their levels
            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))
        
        # Collect values from each level
        for level in range(len(rightmost_value)):
            right_view.append(rightmost_value[level])
        
        return right_view


        
