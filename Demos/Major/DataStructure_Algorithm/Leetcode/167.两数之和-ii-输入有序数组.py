#
# @lc app=leetcode.cn id=167 lang=python3
#
# [167] 两数之和 II - 输入有序数组
#

# @lc code=start
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        s, m, e = 0, 0, len(numbers) - 1

        for x in range(0, e):
            s = x + 1
            e = len(numbers) - 1
            while s < e:
                m = s + e >> 1
                if numbers[m] == target - numbers[x]:
                    return [x + 1, m + 1]
                elif numbers[m] < target - numbers[x]:
                    s = m + 1
                else:
                    e = m
            if numbers[e] == target - numbers[x]:
                return [x + 1, e + 1]
# @lc code=end

# 双指针法

# class Solution:
#     def twoSum(self, numbers: List[int], target: int) -> List[int]:
#         low, high = 0, len(numbers) - 1
#         while low < high:
#             total = numbers[low] + numbers[high]
#             if total == target:
#                 return [low + 1, high + 1]
#             elif total < target:
#                 low += 1
#             else:
#                 high -= 1

#         return [-1, -1]


# 作者：LeetCode-Solution
# 链接：https: // leetcode-cn.com/problems/two-sum-ii-input-array-is-sorted/solution/liang-shu-zhi-he-ii-shu-ru-you-xu-shu-zu-by-leet-2/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
