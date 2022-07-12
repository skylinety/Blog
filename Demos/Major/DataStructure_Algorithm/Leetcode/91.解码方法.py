# @before-stub-for-debug-begin
from python3problem91 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=91 lang=python3
#
# [91] 解码方法
#

# @lc code=start
# class Solution:
#     def numDecodings(self, s: str) -> int:
#         if s[0] == "0":
#             return 0
#         ago = 1
#         pre = 1
#         ret = 1
#         n = len(s)
#         for i in range(1, n):
#             if ((s[i - 1] == "1" or s[i - 1] == "2")):
#                 if s[i] == "0":
#                     ret = ago
#                     ago = pre
#                     pre = ret
#                     continue
#                 if int(s[i]) <= 6:
#                     ret = ago + pre
#                     ago = pre
#                     pre = ret
#                     continue
#             else:
#                 if s[i] == "0":
#                     return 0
#             ret = pre
#             ago = pre
#             pre = ret
#         return ret
                
class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == "0":
            return 0
        ago = 1
        pre = 1
        ret = 1
        n = len(s)
        for i in range(1, n):
            num = int(s[i - 1] + s[i])
            if num == 0 or (num % 10 == 0 and num > 20):
                return 0
            elif num == 20 or num == 10:
                ret = ago
                ago = pre
                pre = ret
                continue
            elif (num > 10 and num < 27):
                ret = ago + pre
                ago = pre
                pre = ret
                continue
            else:
                ret = pre
                ago = pre
                pre = ret
        return ret
                
# @lc code=end

# 问题关键在于前一数字和当前数字是否可以组成新的编码

# 前一个数字1、2
# dp[i]=dp[i-2] 和前一个数字可以组成新编码且当前数字为0
# dp[i]=dp[i-1]+dp[i-2] 和前一个数字可以组成新编码且当前数字1-6
# dp[i]=dp[i-1] 和前一个数字可以组成新编码且当前数字7-9
# 前一个数字非1、2
# 当前数字为0，解码失败
# dp[i]=dp[i-1] 和前一个数字不能组成新编码，当前数字单独编码


# 两位数示意，第一位为前一数字，第二位为当前数字
# 编码失败
# 00 30 40 50 60 70 80 90
# 编码成功
# 新加入数字即可单独编码，又可和前一数字一起编码 11-19, 21-26 dp[i]=dp[i-1]+dp[i-2]
# 新加入数字只可和前一数字一起编码 10,20  dp[i]=dp[i-2]
# 新加入数字只可单独编码 01-09,27-99  dp[i]=dp[i-1]

