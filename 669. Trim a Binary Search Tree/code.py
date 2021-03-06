# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def trimBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: TreeNode
        """
        if root is None:
            return

        left = self.trimBST(root.left, L, root.val)
        right = self.trimBST(root.right, root.val, R)

        if root.val < L:
            return self.trimBST(root.right, L, R)
        if L <= root.val <= R:
            root.left = left
            root.right = right
            return root
        if R < root.val:
            return self.trimBST(root.left, L, R)       