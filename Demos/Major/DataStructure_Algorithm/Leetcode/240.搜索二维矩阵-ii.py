# @before-stub-for-debug-begin
from python3problem240 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=240 lang=python3
#
# [240] 搜索二维矩阵 II
#

# @lc code=start

# 递归与二分查找

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # rowstart,columnstart,rowend,columnend,rowmiddle,columnmiddle
        rs, cs, re, ce = 0, 0, len(matrix) - 1, len(matrix[0]) - 1

        def recMatrix(rs, cs, re, ce):
            rm = rs + re >> 1
            cm = cs + ce >> 1
            if rs > re or cs > ce:
                return False
            if matrix[rm][cm] == target:
                # print(rm, cm)
                return True
            if matrix[rm][cm] > target:
                return recMatrix(rs, cs, re, cm - 1) or recMatrix(rs, cm, rm - 1, ce)
            else:
                return recMatrix(rs, cm + 1, re, ce) or recMatrix(rm + 1, cs, re, cm)

        return recMatrix(rs, cs, re, ce)


# @lc code=end

# 双指针法

# 因为 matrixmatrix 矩阵中每行的元素从左到右升序排列且每列的元素从上到下升序排列，所以可以从左下角（或右上角）开始查找。

# 若当前矩阵的元素值 == target，则直接返回 true。

# 若当前矩阵的元素值 > target，则向上移动一行列不变，即 matrix[i][j] 变为 matrix[i - 1][j]，继续进行比较。

# 若当前矩阵的元素值 < target，则向右移动一列行不变，即 matrix[i][j] 变为 matrix[i][j + 1]，继续进行比较。


# class Solution:
#     def searchMatrix(self, matrix, target):
#         # an empty matrix obviously does not contain `target` (make this check
#         # because we want to cache `width` for efficiency's sake)
#         if len(matrix) == 0 or len(matrix[0]) == 0:
#             return False

#         # cache these, as they won't change.
#         height = len(matrix)
#         width = len(matrix[0])

#         # start our "pointer" in the bottom-left
#         row = height-1
#         col = 0

#         while col < width and row >= 0:
#             if matrix[row][col] > target:
#                 row -= 1
#             elif matrix[row][col] < target:
#                 col += 1
#             else:  # found it
#                 return True

#         return False


# 作者：LeetCode
# 链接：https: // leetcode-cn.com/problems/search-a-2d-matrix-ii/solution/sou-suo-er-wei-ju-zhen-ii-by-leetcode-2/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
