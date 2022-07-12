# @before-stub-for-debug-begin
from python3problem221 import *
from typing import *
# @before-stub-for-debug-end


#
# @lc app=leetcode.cn id=221 lang=python3
#
# [221] 最大正方形
#
# [[1,0,1,0,0],[1,0,1,1,1],[1,1,1,1,1],[1,0,0,1,0]]
# @lc code=start
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:

        m = len(matrix)
        if m == 0:
            return 0
        n = len(matrix[0])
        if n == 0:
            return 0
        l = 0
        dp = list(map(lambda str: int(str), matrix[0]))
        ret = max(dp)

        for i in range(1, m):
            for j in range(n):
                cur = int(matrix[i][j])
                if j == 0:
                    l = cur
                    ret = max(ret, l)
                    continue
                if cur == 0:
                    dp[j - 1] = l
                    l = 0

                if cur == 1:

                    verge = min(l, dp[j -1], dp[j]) ** 0.5 + 1
                    dp[j - 1] = l
                    l = verge ** 2
                    ret = max(ret, l)
                if j == n - 1:
                    dp[j] = l

        return int(ret)

# @lc code=end

# dp[i][j] 以i j 为右下角的组成1的最大正方形值
