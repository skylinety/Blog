# @before-stub-for-debug-begin
from python3problem819 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=819 lang=python3
#
# [819] 最常见的单词
#

# @lc code=start
import re


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraphArr = re.split(
            ' +', re.sub('[^\s\w]', " ", paragraph).lower().strip())
        dict = {}
        for b in banned:
            dict[b] = -1
        ret = ''
        maxCount = 1
        for p in paragraphArr:
            if p in dict and dict[p] == -1:
                continue
            if p not in dict:
                dict[p] = 0
            dict[p] += 1
            if maxCount <= dict[p]:
                maxCount = dict[p]
                ret = p
        return ret
# @lc code=end
