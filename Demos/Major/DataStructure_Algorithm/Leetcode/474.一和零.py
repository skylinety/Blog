# @before-stub-for-debug-begin
from python3problem474 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=474 lang=python3
#
# [474] 一和零
#

# @lc code=start
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:

        # 1行0列
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        for s in strs:
            for i in range(n, -1, -1):
                for j in range(m, -1, -1):
                    c0 = s.count('0')
                    c1 = s.count('1')
                    if j < c0 or i < c1:
                        break
                    dp[i][j] = max(dp[i][j], dp[i - c1][j - c0] + 1)
        
        return dp[n][m]
# @lc code=end
        # dp[i][m][n] = max(dp[i - 1][m][n], dp[i - 1][m - strs[i].count('0')][n - strs[i].count('1')] + 1)
