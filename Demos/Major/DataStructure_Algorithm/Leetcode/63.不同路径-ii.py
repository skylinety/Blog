#
# @lc app=leetcode.cn id=63 lang=python3
#
# [63] 不同路径 II
#
# @before-stub-for-debug-begin
from python3problem63 import *
from typing import *
# @before-stub-for-debug-end

# @lc code=start
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        columnLen = len(obstacleGrid[0])
        rowLen = len(obstacleGrid)
        note = [0] * columnLen
        ret = 0

        # 处理初始上边界并用记事本note保存
        for i,v in enumerate(obstacleGrid[0]):
            if v == 1:
                break
            note[i] = 1

        if rowLen == 1:
            return note[-1]

        for r in range(1, rowLen):
            for c in range(columnLen):

                # 当前位置为障碍物
                if obstacleGrid[r][c] == 1:
                    ret = 0
                    note[c] = 0
                    continue
                # 当前位置位于左边界
                if c == 0:
                    ret = note[c]
                    continue

                # 普通情况
                ret = ret + note[c]
                note[c] = ret

        return ret
# @lc code=end

# dp[r][c]表示到达对应位置拥有的方法数，此时在网格位置用pos标记

# pos处有障碍物 
# dp[r][c] = 0

# pos处在上边界（r == 0）
# dp[r][c] 在上边界第一个障碍物处分界，障碍物左边为1，右边为0


# pos处在左边界（c == 0）
# dp[r][c] = dp[r - 1][c]

# 其他普通情况
# 1: pos只左边有障碍物 dp[r][c] = dp[r][c - 1]
# 2: pos只上边有障碍物 dp[r][c] = dp[r - 1][c]
# 3: pos左边上边都有障碍物 dp[r][c] = 0
# 4: pos都无障碍物 dp[r][c] = dp[r][c - 1] + dp[r - 1][c]


# 普通情况合并
# 1: pos只左边有障碍物 dp[r - 1][c] = 0  dp[r][c] = dp[r][c - 1] + dp[r - 1][c]
# 2: pos只上边有障碍物 dp[r][c - 1] = 0， dp[r][c] = dp[r][c - 1] + dp[r - 1][c]
# 3: pos左边上边都有障碍物 dp[r - 1][c] = 0， dp[r][c - 1] = 0， dp[r][c] = dp[r][c - 1] + dp[r - 1][c]
# 4: pos都无障碍物 dp[r][c] = dp[r][c - 1] + dp[r - 1][c]


# 测试例子 [[0,0,0,0],[0,0,0,0],[1,1,1,0],[0,0,0,0],[0,0,0,0],[1,0,0,0]]
