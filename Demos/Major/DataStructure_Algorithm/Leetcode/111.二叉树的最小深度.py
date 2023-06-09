# @before-stub-for-debug-begin
from python3problem111 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=111 lang=python3
#
# [111] 二叉树的最小深度
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        # tree = [root]
        if root is None:
            return 0
        ret = 1
        level = [root]
        while len(level):
            # newLevel = []
            # node = tree.pop(0)
            # for node in level:
            #     if node:
            for _ in range(len(level)):
                node = level.pop(0)
                if node:
                    level.append(node.left)
                    level.append(node.right)
                    if node.left is None and node.right is None:
                        return ret
            ret += 1
            # level = newLevel
            # if node.left is None and node.right is None:
            #     return ret
            # node.left and tree.append(node.left)
            # node.right and tree.append(node.right)

# @lc code=end

