# @before-stub-for-debug-begin
from python3problem647 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=647 lang=python3
#
# [647] 回文子串
#

# @lc code=start
# 动态规划
class Solution:
    def countSubstrings(self, s: str) -> int:
        l = len(s)
        # base = [[False] * l for _ in range(l)]
        base = [[False] * l for _ in range(l)]
        ret = l

        for j in range(l):
            for i in range(j):
                if s[i] == s[j]:
                    # 当首尾相等且长度不超过3时
                    if j - i < 3:
                        base[i][j] = True
                        ret += 1
                        continue
                    if base[i + 1][j - 1]:
                        base[i][j] = True
                        ret += 1

        return ret
# @lc code=end

# 暴力解法
class Solution:
    def countSubstrings(self, s: str) -> int:
        l = len(s)
        ret = l
        for i in range(1, l):
            for j in range(i):
                part = s[j:i+1]
                if part[::-1] == part:
                    ret += 1
        return ret
