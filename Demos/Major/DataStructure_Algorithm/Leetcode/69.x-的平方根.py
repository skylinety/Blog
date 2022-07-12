# @before-stub-for-debug-begin
from python3problem69 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=69 lang=python3
#
# [69] x 的平方根
#

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        s = 0
        e = x
        m = 0
        while s < e:
            m = (s + e) // 2
            if m**2 == x:
                return m
            if m**2 < x:
                s = m + 1   
            else:
                e = m
            
        return s if s ** 2 <= x else s - 1
        
# @lc code=end

