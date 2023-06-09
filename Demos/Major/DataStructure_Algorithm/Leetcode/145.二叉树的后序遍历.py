#
# @lc app=leetcode.cn id=145 lang=python3
#
# [145] 二叉树的后序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # ret = []
        # def traversal(root):
        #     if not root:
        #         return
        #     if root.left:
        #          traversal(root.left)
        #     if root.right:
        #          traversal(root.right)
        #     ret.append(root.val)
        # traversal(root)
        # return ret
        ret = []
        if not root:
            return ret

        def traverse(root):
            root.left and traverse(root.left)
            root.right and traverse(root.right)
            ret.append(root.val)
        traverse(root)
        return ret
# @lc code=end

