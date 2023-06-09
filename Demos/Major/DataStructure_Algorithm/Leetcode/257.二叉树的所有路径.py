#
# @lc app=leetcode.cn id=257 lang=python3
#
# [257] 二叉树的所有路径
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        ret = []
        def traverse(root, path):
            if not root:
                return
            if path != '':
                path += '->'
            path += str(root.val)
            if not (root.left or root.right):
                ret.append(path)
                return
            
            traverse(root.left, path)
            traverse(root.right, path)

        traverse(root, '')
        return ret
# @lc code=end

