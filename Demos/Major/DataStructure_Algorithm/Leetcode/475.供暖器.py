# @before-stub-for-debug-begin
from python3problem475 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=475 lang=python3
#
# [475] 供暖器
#

# @lc code=start


class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        def quickSort(nums, s, e):
            if e - s < 1:
                return
            # pivot = nums[s]
            S, E = s + 1, e
            while S <= E:
                while S <= E and nums[S] <= nums[s]:
                    S += 1
                while S <= E and nums[E] >= nums[s]:
                    E -= 1
                if S < E:
                    nums[S], nums[E] = nums[E], nums[S]
                    S += 1
                    E -= 1
            nums[E], nums[s] = nums[s], nums[E]
            if s < E - 1:
                quickSort(nums, s, E - 1)
            if S < e:
                quickSort(nums, S, e)

        def binarySearch(nums, target):
            s, e = 0, len(nums) - 1
            while s < e:
                m = s + e >> 1
                if target > nums[m]:
                    s = m + 1
                else:
                    e = m
            return s

        # quickSort(heaters, 0, len(heaters) - 1)
        heaters.sort()

        ret = 0
        for house in houses:
            pos = binarySearch(heaters, house)

            if pos > 0:
                ret = max(ret, min(abs(heaters[pos] - house),
                          abs(house - heaters[pos - 1])))
            else:
                ret = max(ret, abs(heaters[pos] -
                          house))

        return ret
# @lc code=end
