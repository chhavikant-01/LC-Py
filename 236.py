# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        # Dictionary to store parent pointers
        parent = {root: None}
        stack = [root]
        
        # First DFS to find both nodes and build parent pointers
        while p not in parent or q not in parent:
            node = stack.pop()
            
            if node.left:
                parent[node.left] = node
                stack.append(node.left)
            if node.right:
                parent[node.right] = node
                stack.append(node.right)
        
#         3
#       / \
#      5   1
#     / \   \
#    6   2   8
#       / \
#      7   4
# parent = {
#     3: None,   # Root has no parent
#     5: 3,      # 5's parent is 3
#     1: 3,      # 1's parent is 3
#     6: 5,      # 6's parent is 5
#     2: 5,      # 2's parent is 5
#     8: 1,      # 8's parent is 1
#     7: 2,      # 7's parent is 2
#     4: 2       # 4's parent is 2
# }
        
        # First, we create an empty set to store all ancestors of p (node 7)
        ancestors = set()

        # This while loop starts at p (node 7) and goes up the tree, 
        # adding each node it visits to the ancestors set
        while p:
            ancestors.add(p)    # Add current node
            p = parent[p]      # Move up to parent

        # After this loop, ancestors contains: {7, 2, 5, 3}
        # Because we went: 7 -> 2 -> 5 -> 3 -> None
        
        # Starting at q (node 4), we keep moving up the tree
        # until we find the first node that's also in our ancestors set
        while q not in ancestors:
            q = parent[q]

        # The path we follow is: 4 -> 2
        # We stop at 2 because it's in our ancestors set
        
        return q
