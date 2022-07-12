#
# @lc app=leetcode.cn id=32 lang=python3
#
# [32] 最长有效括号
#

# @lc code=start
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        l = len(s)
        dp = [[False] * l for _ in range(l)]
        ret = 0
        for i in range(1, l + 1):
            for j in range(i):
                dp[i][j] = dp[i + 1][j - 1]

                if s[i] == '(' and s[j] == ')':
                    if dp[i][j]:
                        ret = max(ret, j - i + 1)
                    if j - i == 1:
                        dp[i][j] = True
                        continue
                if s[i] == ')' and s[j] == '(':
                    if j - i == 1:
                        dp[i][j] = True
                        continue

                dp[i][j] = False

        return ret
# @lc code=end

# dp[i][j]表示i 到 j是否字符对称
# dp[i][j]=dp[i + 1][j - 1] & s[i] == '(' $ s[j] == ')'
