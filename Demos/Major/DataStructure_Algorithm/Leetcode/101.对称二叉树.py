# @before-stub-for-debug-begin
from python3problem101 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=101 lang=python3
#
# [101] 对称二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        # 递归
        # def traverse(leftTree: Optional[TreeNode], rightTree: Optional[TreeNode]):
        #     if leftTree is None or rightTree is None:
        #         return leftTree == rightTree
        #     return leftTree.val == rightTree.val and traverse(leftTree.left, rightTree.right) and traverse(leftTree.right, rightTree.left)

        # return traverse(root.left, root.right)

        # 迭代
        if root.left == root.right:
            return True

        queue = [root.left, root.right]
        while queue and len(queue):

            # if len(queue) % 2 == 1:
            #     return False

            rear = len(queue) - 1
            head = 0
            headQueue = []
            rearQueue = []

            while head < rear:
                headNode = queue[head]
                rearNode = queue[rear]

                # 处理出现一个None的情况
                if headNode is None or rearNode is None:
                    if headNode != rearNode:
                        return False

                # 处理不出现None的情况
                if headNode != rearNode:
                    if headNode.val != rearNode.val:
                        return False
                    else:
                        headQueue.append(headNode.left)
                        headQueue.append(headNode.right)
                        rearQueue.insert(0, rearNode.right)
                        rearQueue.insert(0, rearNode.left)
                head += 1
                rear -= 1

            headQueue.extend(rearQueue)
            queue = headQueue

        return True

# 利用层序遍历，利用双指针，对比每一层的首尾
        # @lc code=end
