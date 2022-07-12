# @before-stub-for-debug-begin
from python3problem139 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=139 lang=python3
#
# [139] 单词拆分
#

# @lc code=start
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        ls = len(s) + 1
        lw = len(wordDict)
        dp = [False] * ls
        dp[0] = True
        for i in range(0, ls):
            for j in range(0, lw):
                pos = i - len(wordDict[j])
                if pos < 0:
                    continue
                sub = s[pos:i]
                if sub != wordDict[j]:
                    continue
                # if pos == 0:
                #     dp[i] = True
                # if pos > 0:
                dp[i] = dp[pos]
                if dp[i]:
                    break

        return dp[-1]

# @lc code=end

# dp[i] 表示i处截取之前的字符是否拆分成功
# dp[i] = dp[i - 1] && s[i:1] in singleDict 考虑dict全是单字母的情况
# dp[i] = dp[i - len(wordDict[j])] 考虑dict全是word的情况

# ccccffxeen  f en fxe cccc
