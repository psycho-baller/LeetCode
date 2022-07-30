#
# @lc app=leetcode id=572 lang=python3
#
# [572] Subtree of Another Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def is_equal(self, root, subRoot):
        if not root and not subRoot:
            return True
        elif not root or not subRoot or root.val != subRoot.val:
            return False
        return (self.is_equal(root.left, subRoot.left) and self.is_equal(root.right, subRoot.right))
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        ### Order is important ###
        if not subRoot:
            return True
        if not root:
            return False
        ###                    ###
        if self.is_equal(root, subRoot):
            return True
        return (self.isSubtree(root.left, subRoot) or
        self.isSubtree(root.right, subRoot))
# @lc code=end

