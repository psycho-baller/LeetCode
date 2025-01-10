#
# @lc app=leetcode id=450 lang=python3
#
# [450] Delete Node in a BST
#


# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def searchThenDelete(root: TreeNode, key: int) -> bool:
            # if root.val == key:
            #     pass
            if key == root.left.val:
                if root.left.left:
                    root.left = root.left.left
                elif root.left.right:
                    root.left = root.left.right
                else:
                    root.left = None
                return True

            elif key == root.right.val:
                root.right = (
                    root.right.left
                    if root.right.left
                    else (root.right.right if root.right.right else None)
                )
                return True
            if key > root.val:
                searchThenDelete(root.right, key)
            else:
                searchThenDelete(root.left, key)

        if not root:
            return root
        searchThenDelete(root, key)
        return root


# @lc code=end
