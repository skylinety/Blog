# @before-stub-for-debug-begin
from python3problem403 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=403 lang=python3
#
# [403] 青蛙过河
#

# @lc code=start

# dp[x][k]表示到x位置时跳跃k步，x在代码中示意为i或j j>i
# dp[j][k] = dp[i][k] or dp[i][k - 1] or dp[i][k + 1]
class Solution:
    def canCross(self, stones: List[int]) -> bool:
        t = len(stones)
        # t = stones[-1] + 1
        # ret = True
        # ago = stones[0]
        # pre = stones[1]
        if stones[1] != 1:
            return False
        # if stones[1] - stones[0] > 2:
        #     return False
        dp = [[False] * t for _ in range(t)]

        dp[1][1] = True
        for j in range(2, t):
            for i in range(j - 1, -1, -1):
                # if i not in stones or j not in stones:
                #     dp[i][j] = False
                #     continue
                k = stones[j] - stones[i]
                if k > i + 1:
                    break;

                dp[j][k] = dp[i][k] or dp[i][k - 1] or dp[i][k + 1]

        for n in dp[t - 1]:
            if n:
                return True

        return False
# @lc code=end
# [0,1,2,3,4,8,9,11]
# [0,1,3,5,6,8,12,17]
# 背包问题
# dp[i][j]表示由i跳到j i < j
# dp[i][j] = dp[i - j + i][i] or
#            dp[i - j + i - 1][i] or
#            dp[i - j + i + 1][i]

# MemoryError
# test case [0,1,2147483647]
# code

# class Solution:
#     def canCross(self, stones: List[int]) -> bool:
#         # l = len(stones)
#         t = stones[-1] + 1
#         # ret = True
#         # ago = stones[0]
#         # pre = stones[1]
#         if stones[1] != 1:
#             return False
#         # if stones[1] - stones[0] > 2:
#         #     return False
#         dp = [[False] * t for _ in range(t)]

#         dp[0][1] = True
#         for j in range(2, t):
#             for i in range(j):
#                 if i not in stones or j not in stones:
#                     dp[i][j] = False
#                     continue
#                 span = j - i
#                 dp[i][j] = dp[i - span][i] or dp[i -
#                                                  span - 1][i] or dp[i - span + 1][i]

#         for n in dp:
#             if n[-1]:
#                 return True

#         return False
