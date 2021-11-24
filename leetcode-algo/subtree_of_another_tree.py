# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def areSame(self, root1: TreeNode, root2: TreeNode) -> bool:
        if root1 is None and root2 is None: return True
        if root1 is None or root2 is None: return False
        return root1.val == root2.val and self.areSame(root1.left, root2.left) and self.areSame(root1.right, root2.right)

    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        if root is None: return False
        if root.val == subRoot.val and self.areSame(root, subRoot): return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
