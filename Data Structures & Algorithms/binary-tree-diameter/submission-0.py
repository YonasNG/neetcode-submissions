# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        output = 0

        def height(node):
            if not node:
                return 0
            
            left = height(node.left)
            right = height(node.right)
            diameter = left + right

            nonlocal output
            output = max(output, diameter)

            return 1 + max(left, right)

        height(root)
        return output

    # Time Complexity: O(n), where n is the number of nodes
    # Space Complexity: O(h), where h is the height of the tree (recursion stack)
