# @before-stub-for-debug-begin
from python3problem140 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=140 lang=python3
#
# [140] 单词拆分 II
#

# @lc code=start
class Solution:

    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        ls = len(s) + 1
        lw = len(wordDict)
        dp = [[]for _ in range(ls)]
        for i in range(0, ls):
            for j in range(0, lw):
                pos = i - len(wordDict[j])
                if pos < 0:
                    continue
                sub = s[pos:i]
                if sub != wordDict[j]:
                    continue
                if pos == 0:
                    dp[i].append(sub)
                    continue
                dp[i] += list(map(lambda str: str + ' ' + sub, dp[pos]))
                # dp[i] += dp[pos].map(v)

        return dp[-1]
# @lc code=end

