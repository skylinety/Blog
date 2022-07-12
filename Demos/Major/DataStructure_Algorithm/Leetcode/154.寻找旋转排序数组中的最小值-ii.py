#
# @lc app=leetcode.cn id=154 lang=python3
#
# [154] 寻找旋转排序数组中的最小值 II
#

# @lc code=start
class Solution:
    def findMin(self, nums: List[int]) -> int:

        if nums[0] < nums[-1]:
            return nums[0]

        s = 0
        e = len(nums) - 1

        m = 0

        while s < e:
            m = (s + e) // 2
            if nums[s] == nums[e] == nums[m]:
                s += 1
                e -= 1
                continue;
            if nums[m] <= nums[e]:
                e = m
            else:
                s = m + 1

        return nums[s]

# @lc code=end

