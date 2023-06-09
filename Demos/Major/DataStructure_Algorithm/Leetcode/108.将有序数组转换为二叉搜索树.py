#
# @lc app=leetcode.cn id=108 lang=python3
#
# [108] 将有序数组转换为二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def folio(nums):
            pos = len(nums)//2
            val = nums[pos]
            root = TreeNode(val)
            leftNums = nums[:pos]
            rightNums = nums[pos+1:]
            if len(leftNums):
                root.left = folio(leftNums)
            if len(rightNums):
                root.right = folio(rightNums)
            return root
        return folio(nums)
            

# @lc code=end
