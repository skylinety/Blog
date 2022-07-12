# @before-stub-for-debug-begin
from python3problem312 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=312 lang=python3
#
# [312] 戳气球
#

# @lc code=start

# not solved
# recommand settlement
# https: // leetcode-cn.com/problems/burst-balloons/solution/zhe-ge-cai-pu-zi-ji-zai-jia-ye-neng-zuo-guan-jian-/

class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        l = len(nums)
        dp = [[0] * l for _ in range(l)]
        # for i, n in enumerate(nums):
        #     dp[i][i] = n
        for j in range(1, l):
            for i in range(j):
            # for i in range(j - 1):
                m =  max(nums[i], nums[j])
                if j - i == 1:
                    dp[i][j] = nums[i] * nums[j] + m
                    continue
                pm = max(nums[i + 1], nums[j - 1])
                dp[i][j] = dp[i + 1][j - 1] + pm * nums[i] * nums[j] + nums[i] * nums[j] + m

        return dp[0][l - 1]


# @lc code=end
# 边界must最后搓爆
# dp[i][j] 锉爆 i 到 j 后获得的最大数
# last 表示上轮最后一个值
# dp[i][j]=dp[i - 1][j - 1] + last * num[i]num[j] + num[i]num[j]
# last = max(num[i], num[j] )
# dp[i][j] += last


# 如何想到这样定义状态？

# 大部分DP，基本还是问啥就咋定义，范围：从前到后，值：所求最值。
# dp[i][j], 范围在开区间(i, j)能得到的硬币数
# 如何想到这样转移状态？

# dp问题，比较好的办法是自底向上(从数组下标0出发往后推) == 从初始推到最终 == 从小问题推到大问题
# 那么我们考虑如何转移时，可以假设小问题都求好了，所以从最后一步考虑，即本题的戳最后一个气球，合并石子中的最后两坨的合并
# 本题的区间很特别，为啥开区间，为啥两遍加1？

# 算是个处理边界的技巧吧，我也说不出为啥，但如果不这样处理，需要处理-1和len的越界就会让处理边界代码很多
# 而依着题目描述的两边当1处理，加上后，又不能戳这两个假边界，所以就开区间了
# 本题的类型：【区间DP】。求dp[i][j]代码套路就是2层循环起步，第一层是遍历 i 到 j 的**宽度 **，第二层是遍历左端点 i(由第一层的宽度和第二层的左端点，可等价等到 j 右端点)。这样从小到大得到最终解
