# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        def getLeaves(root):
            if not root:
                return []
            
            leaves = []
            stack = [root]
            
            while stack:
                node = stack.pop()
                
                # If we find a leaf, add it to our sequence
                if not node.left and not node.right:
                    leaves.append(node.val)
                    continue
                
                # Add right child first so it's processed after left
                # (stack is LIFO - Last In, First Out)
                if node.right:
                    stack.append(node.right)
                if node.left:
                    stack.append(node.left)
            
            return leaves
    
        return getLeaves(root1) == getLeaves(root2)
            
