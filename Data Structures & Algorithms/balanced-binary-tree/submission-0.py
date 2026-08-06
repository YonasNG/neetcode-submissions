# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def height(node):
            # An empty subtree has height 0
            if not node:
                return 0

            # Recursively get the height of the left and right subtree
            # Return -1 if it is unbalanced
            left = height(node.left)
            if left == -1:
                return -1

            right = height(node.right)
            if right == -1:
                return -1
            
            # If the current node's subtrees differ in height by more than 1
            # They are unbalanced
            if abs(left - right) > 1:
                return -1
            
            # Return the height of the current subtree
            return 1 + max(left, right)
        
        return height(root) != -1

        # Time Complexity: O(n), where n is the number of nodes
        # Space Complextiy: O(h), where h is the height of the tree

