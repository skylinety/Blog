# @before-stub-for-debug-begin
from python3problem494 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=494 lang=python3
#
# [494] 目标和
#

# @lc code=start


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        sumRet = sum(nums)
        lenNums = len(nums)
        sumPositive = (sumRet + target) // 2
        if abs(target) > sumRet or (sumRet + target) % 2 != 0:
            return 0

        notes = [0] * (sumPositive + 1)

        if nums[0] <= sumPositive:
            notes[nums[0]] = 1

        notes[0] = 2 if nums[0] == 0 else 1

        for i in range(1, lenNums):
            for s in range(sumPositive, nums[i]-1, -1):
                notes[s] = notes[s] + notes[s - nums[i]]

        return notes[-1]
# @lc code=end
# dp[i][j]表示前i个数里组合获取到j值得方法数
# dp[i][j] = dp[i - 1][j - nums[i]] + dp[i - 1】[j]


# solution 1
# dp[i][j]表示前i个数用完可以组合得到j数值的方式
# dp[i][j] = dp[i - 1][j - nums[i]] 解数量
        #           + dp[i - 1][j + nums[i]] 解数量

# class Solution:
#     def findTargetSumWays(self, nums: List[int], target: int) -> int:
#         inputs = map(lambda n: -n, nums)

#         m = max(nums)

#         top = sum(nums)
#         bottom = - top
#         if target > top or target < bottom:
#             return 0
#         pre = {
#             # nums[0]: 1,
#             # -nums[0]: 1
#         }

#         for n in range(top, bottom - 1, -1):
#             pre[n] = 0
#             # now[n] = 0

#         pre[nums[0]] = 1
#         pre[-nums[0]] = 1
#         if nums[0] == 0:
#             pre[0] = 2

#         for i in range(1, len(nums)):
#             now = {
#             }
#             for j in range(top, bottom - 1, -1):
#                 l = 0
#                 r = 0

#                 if j - nums[i] >= bottom:
#                     l = pre[j - nums[i]]
#                 if j + nums[i] <= top:
#                     r = pre[j + nums[i]]
#                 now[j] = l + r
#             pre = now

#         return pre[target]
