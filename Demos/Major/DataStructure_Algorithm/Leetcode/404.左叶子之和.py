#
# @lc app=leetcode.cn id=404 lang=python3
#
# [404] 左叶子之和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        # self.ret = 0
        ret = 0
        def traverse(root, isLeft):
            if not root:
                return
            if isLeft and not (root.left or root.right):
                nonlocal ret
                ret += root.val
                # self.ret += root.val
            traverse(root.left, True)
            traverse(root.right, False)
            
        traverse(root, False)
        return ret
        # return self.ret
# @lc code=end

