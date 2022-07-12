# @before-stub-for-debug-begin
from python3problem322 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=322 lang=python3
#
# [322] 零钱兑换
#

# @lc code=start
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount is 0:
            return 0
        l = len(coins)
        dp = [[sys.maxsize] * (amount + 1) for _ in range(l)]
        for n in range(1, amount + 1):
            if n % coins[0] == 0:
                dp[0][n] = n / coins[0]

        for i in range(1, l):
            for j in range(1, amount + 1):
                if j - coins[i] < 0:
                    dp[i][j] = dp[i - 1][j]
                    continue
                if j - coins[i] == 0:
                    dp[i][j] = 1
                    continue
                dp[i][j] = min(dp[i - 1][j - coins[i]] + 1,
                               dp[i - 1][j], dp[i][j - coins[i]] + 1)
                # a = dp[i][j] if dp[i][j] > 0 else sys.maxsize
                # b = dp[i - 1][j - coins[i]] + 1 if dp[i - 1][j - coins[i]] > 0 else sys.maxsize
                # c = dp[i][j - coins[i]] + 1 if dp[i][j - coins[i]] > 0 else sys.maxsize

                # dp[i][j] = min(a, b, c)

                # dp[i][j] = min(dp[i - 1][j - coins[i]] + 1,
                #                dp[i - 1][j], dp[i][j - coins[i]] + 1)
                # dp[i][j] = min(dp[i - 1][j - coins[i]], dp[i][j - coins[i]]) + 1
                # if dp[i - 1][j] > 0:
                #     dp[i][j] = min(dp[i][j], dp[i - 1][j])
        return int(dp[l - 1][amount]) if dp[l - 1][amount] < sys.maxsize else -1

# @lc code=end
# dp[i][j] 表示前i个硬币组成值j的最少硬币数目
# 第i枚银币用或不用
# j - coins[i] == 0 用 且dp[i][j]=1
# j - coins[i] < 0 不用 且dp[i][j] = dp[i - 1][j]
# j - coins[i] > 0 可用
# dp[i - 1][j - coins[i]] + 1  只用一次coins[i]
# dp[i][j - coins[i]] + 1  用多次coins[i]
# dp[i][j] = min(dp[i - 1][j - coins[i]] + 1, dp[i - 1][j], dp[i][j - coins[i]] + 1)



# 推荐解法
# class Solution:
#     def coinChange(self, coins: List[int], amount: int) -> int:
#         dp = [float('inf')] * (amount + 1)
#         dp[0] = 0

#         for coin in coins:
#             for x in range(coin, amount + 1):
#                 dp[x] = min(dp[x], dp[x - coin] + 1)
#         return dp[amount] if dp[amount] != float('inf') else -1


# 作者：LeetCode-Solution
# 链接：https: // leetcode-cn.com/problems/coin-change/solution/322-ling-qian-dui-huan-by-leetcode-solution/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
