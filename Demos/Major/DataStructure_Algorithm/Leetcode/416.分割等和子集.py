# @before-stub-for-debug-begin
from python3problem416 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=416 lang=python3
#
# [416] 分割等和子集
#

# @lc code=start
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        left = 0
        right = sum(nums)
        for n in nums:
            left += n
            right -= n
            if left == right:
                return True

        return False
# @lc code=end

# dp
