#
# @lc app=leetcode.cn id=162 lang=python3
#
# [162] 寻找峰值
#

# @lc code=start
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        s,m,e = 0, 0, len(nums) - 1
        
        while s < e:
            m = s + e >> 1
            if nums[m] < nums[m + 1]:
                s = m + 1
            else:
                e = m

        return e
# @lc code=end

