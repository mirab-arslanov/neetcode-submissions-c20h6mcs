# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSubtree(self, root, subRoot) -> bool:
        if not subRoot: return True
        if not root: return False
        if self.isSameTree(root, subRoot):
            return True
        
        le = self.isSubtree(root.left, subRoot)
        r = self.isSubtree(root.right, subRoot)
        return le or r

    def isSameTree(self, p, q):
        if not p and not q:
            return True
        if (not p or not q) or p.val != q.val:
            return False
        left = self.isSameTree(p.left, q.left)
        right = self.isSameTree(p.right, q.right)
        return left and right