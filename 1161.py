# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        queue = deque([root])
        current_level = 1           # Start at level 1
        max_sum = float('-inf')     # Track highest sum seen
        max_level = 1              # Track level with highest sum
        
        while queue:
            # Get number of nodes at this level
            level_size = len(queue)
            level_sum = 0          # Track sum for current level
            
            # Process all nodes at current level
            for _ in range(level_size):
                node = queue.popleft()
                level_sum += node.val
                
                # Add children to process in next level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            # Update max if this level's sum is larger
            # Use <= because we want smallest level if there's a tie
            if level_sum > max_sum:
                max_sum = level_sum
                max_level = current_level
                
            current_level += 1
        
        return max_level
        
