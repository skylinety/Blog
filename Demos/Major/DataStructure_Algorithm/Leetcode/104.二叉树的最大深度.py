#
# @lc app=leetcode.cn id=104 lang=python3
#
# [104] 二叉树的最大深度
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # if root is None:
        #     return 0
        # ret = 0
        # level = [root]

        # while len(level):
        #     for _ in range(len(level)):
        #         node = level.pop(0)
        #         node.left and level.append(node.left)
        #         node.right and level.append(node.right)
        #     ret += 1

        # return ret

        def dfs(root):
            if not root:
                return 0
            return max(dfs(root.left), dfs(root.right)) + 1
        return dfs(root)
# @lc code=end
