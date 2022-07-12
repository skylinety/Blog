# @before-stub-for-debug-begin
from python3problem5 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        l = len(s)
        base = [[False] * l for _ in range(l)]
        start = 0
        span = 0

        # j表示左边界，i表示右边界，其与左下状态有关，则先遍历列，记录左下的值
        for j in range(l):
            # for i in range(j): 会忽略掉i==j的情况，但是i==j不影响最终题解 
            for i in range(j + 1):
                if s[i] == s[j]:
                    # 当首尾相等且长度不超过3时
                    if j - i < 3:
                        base[i][j] = True
                        if j - i > span:
                            start = i
                            span = j - i
                        continue
                    if base[i + 1][j - 1]:
                        base[i][j] = True
                        if j - i > span:
                            start = i
                            span = j - i


        return s[start:start + span + 1]

# @lc code=end


# dp[i][j]表示第到j字符串是否回文
# dp[i][j]=dp[i+1][j-1] & s[i]==s[j]  与二维数组左下状态有关


# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         n = len(s)
#         if n < 2:
#             return s

#         max_len = 1
#         begin = 0
#         # dp[i][j] 表示 s[i..j] 是否是回文串
#         dp = [[False] * n for _ in range(n)]
#         for i in range(n):
#             dp[i][i] = True

#         # 递推开始
#         # 先枚举子串长度
#         for L in range(2, n + 1):
#             # 枚举左边界，左边界的上限设置可以宽松一些
#             for i in range(n):
#                 # 由 L 和 i 可以确定右边界，即 j - i + 1 = L 得
#                 j = L + i - 1
#                 # 如果右边界越界，就可以退出当前循环
#                 if j >= n:
#                     break

#                 if s[i] != s[j]:
#                     dp[i][j] = False
#                 else:
#                     if j - i < 3:
#                         dp[i][j] = True
#                     else:
#                         dp[i][j] = dp[i + 1][j - 1]

#                 # 只要 dp[i][L] == true 成立，就表示子串 s[i..L] 是回文，此时记录回文长度和起始位置
#                 if dp[i][j] and j - i + 1 > max_len:
#                     max_len = j - i + 1
#                     begin = i
#         return s[begin:begin + max_len]
