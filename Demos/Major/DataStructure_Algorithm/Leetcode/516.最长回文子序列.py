# @before-stub-for-debug-begin
from python3problem516 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=516 lang=python3
#
# [516] 最长回文子序列
#

# @lc code=start
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        if s == '':
            return 0

        l = len(s)
        base = [[0] * l for _ in range(l)]
        ret = 1
        for i in range(l):
            base[i][i] = 1

        for j in range(1, l):
            for i in range(j - 1, -1, -1):
                if s[i] != s[j]:
                    base[i][j] = max(base[i + 1][j], base[i][j - 1])
                else:
                    if j - i < 3:
                        base[i][j] = j - i + 1
                    else: 
                        base[i][j] = base[i + 1][j - 1] + 2

                ret = ret if ret > base[i][j] else base[i][j]

        return ret
# @lc code=end

# 创建二维数组，只有对角线右上部分有效。dp[i][j]表示从i到j最大子串
# 的长度。i表示左边界，j表示右边界，在二维数组中，根据情况划分，dp[i][j]
# 与dp[i+1][j],dp[i][j - 1],dp[i + 1][j - 1]有关，位置分别在正下，正左，左下
# 则遍历方式需要采取遍历列（j），每列值由大到小
# j - i < 3 是特殊处理 特例如sas ss这两种情况
