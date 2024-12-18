# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
                # Dictionary to store the running sum -> frequency mapping
        # Initialize with 0:1 to handle paths that start from root
        prefix_sums = {0: 1}
        
        def dfs(node: TreeNode, current_sum: int) -> int:
            if not node:
                return 0
            
            # Add current node's value to our running sum
            current_sum += node.val
            
            # Check if we have any prefix sum that, when subtracted from 
            # current_sum, gives us our target
            # This means: current_sum - x = targetSum
            # Therefore: x = current_sum - targetSum
            target_prefix = current_sum - targetSum
            
            # Get the count of valid paths ending at current node
            path_count = prefix_sums.get(target_prefix, 0)
            
            # Add current sum to our prefix_sums dictionary
            prefix_sums[current_sum] = prefix_sums.get(current_sum, 0) + 1
            
            # Recursively explore left and right subtrees
            count = (path_count + 
                    dfs(node.left, current_sum) + 
                    dfs(node.right, current_sum))
            
            # Remove current sum from prefix_sums when backtracking
            prefix_sums[current_sum] -= 1
            if prefix_sums[current_sum] == 0:
                del prefix_sums[current_sum]
                
            return count
            
        return dfs(root, 0)
