# @before-stub-for-debug-begin
from python3problem501 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=501 lang=python3
#
# [501] 二叉搜索树中的众数
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 中序遍历二叉搜索树等于遍历有序数组

class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        ret = []
        pre = 0
        times = 0
        max = 0
        def traverse(root):
            nonlocal ret
            nonlocal times
            nonlocal max
            nonlocal pre
            if not root:
                return
            traverse(root.left)

            if root.val == pre:
                times += 1
            else:
                times = 1
            if times == max:
                ret.append(root.val)
            if times > max:
                max = times
                ret = [root.val]
            pre = root.val

            traverse(root.right)
        traverse(root)
        return ret

# @lc code=end

