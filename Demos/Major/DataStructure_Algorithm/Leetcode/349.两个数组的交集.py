# @before-stub-for-debug-begin
from python3problem349 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=349 lang=python3
#
# [349] 两个数组的交集
#

# @lc code=start


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # 冒泡排序
        # 外层循环确定轮次，内层循环交换位置
        # 每一轮通过不断对比交换位置来将该轮最大（小）值上浮（下沉）到对应轮位置
        # def bubbleSort(nums):
        #     for i in range(len(nums)):
        #         for j in range(i + 1, len(nums)):
        #             if nums[i] > nums[j]:
        #                 nums[i], nums[j] = nums[j], nums[i]
        #     return nums

        # 冒泡交换判定优化
        # def optimizeBubbleSort(nums):
        #     for i in range(len(nums)):
        #         swap = False
        #         print(i)
        #         for j in range(i + 1, len(nums)):
        #             if nums[i] > nums[j]:
        #                 nums[i], nums[j] = nums[j], nums[i]
        #                 swap = True
        #         if not swap:.

        #             return nums
        #     return nums

        # 选择排序
        # 外层循环确定轮次，内层循环确定最值
        # 找出每一轮的最值并放在该轮次位置处
        # def selectionSort(nums ):
        #     for i in range(len(nums)):
        #         pos = i
        #         for j in range(i + 1, len(nums)):
        #             if nums[pos] > nums[j]:
        #                 pos = j
        #         nums[i], nums[pos] = nums[pos], nums[i]
        #     return nums

        # 插入排序
        # 外层循环确定插入值，内层循环确定插入位置
        # 将list分为两部分，前部分作为已排序部分并向其中插入值，注意值的移动
        # def insertionSort(nums):
        #     for i in range(1, len(nums)):
        #         if nums[i] < nums[i - 1]:
        #             j = i - 1
        #             aim = nums[i]
        #             while aim < nums[j] and j > -1:
        #                 nums[j + 1] = nums[j]
        #                 j -= 1
        #             nums[j + 1] = aim
        #     return nums

        # 插入排序哨兵优化
        # def sentryInsertionSort(nums):
        #     nums.append(nums[0])
        #     for i in range(1, len(nums)):
        #         if nums[i] < nums[i - 1]:
        #             j = i - 1
        #             nums[0] = nums[i]
        #             while nums[0] < nums[j]:
        #                 nums[j + 1] = nums[j]
        #                 j -= 1
        #             nums[j + 1] = nums[0]
        #     return nums[1:]

        # 插入排序折半优化
        # def binaryInsertionSort(nums):
        #     # nums.append(nums[0])
        #     for i in range(1, len(nums)):
        #         if nums[i] < nums[i - 1]:
        #             aim = nums[i]
        #             s,m,e = 0, 0, i - 1
        #             while s < e:
        #                 m = s+ e >> 1
        #                 if aim > nums[m]:
        #                     s = m + 1
        #                 else:
        #                     e = m
        #             j = i
        #             while j > e:
        #                 nums[j] = nums[j - 1]
        #                 j -= 1
        #             nums[e] = aim
        #     return nums

        # 归并排序
        # 归并排序的主要思想是分治法
        # 将n个元素从中间切开，分成两部分。（左右可能长度差1）
        # 递归分解，直到所有部分的元素个数都为1
        # 从最底层开始逐步向上合并两个排好序的数列。
        # 并
        # def mergeSorted(nums1, nums2):
        #     nums = []
        #     i, j = 0, 0
        #     l = len(nums2)
        #     while i < len(nums1):
        #         if nums1[i] < nums2[j]:
        #             nums.append(nums1[i])
        #             i += 1
        #         else:
        #             nums.append(nums2[j])
        #             j += 1
        #         if (j == l):
        #             break
        #     return nums + nums1[i:] + nums2[j:]
        # # 归
        # def recursionMergeSort(nums):
        #     l = len(nums)
        #     if l < 2:
        #         return nums
        #     else:
        #         m = l // 2
        #         return mergeSorted(recursionMergeSort(nums[:m]), recursionMergeSort(nums[m:]))

        # 快排取中值1
        # def quickSort(nums):
        #     if len(nums) < 2:
        #         return nums

        #     # print(s,e)
        #     # m可取数列中任意数，此处取中位
        #     m = len(nums) // 2
        #     pivot = nums[m]
        #     del nums[m]
        #     s, e = 0, len(nums) - 1
        #     while s <= e:
        #         if nums[s] > pivot and nums[e] < pivot:
        #             nums[s], nums[e] = nums[e], nums[s]
        #             s += 1
        #             e -= 1
        #             continue
        #         if nums[s] <= pivot:
        #             s += 1
        #         if nums[e] >= pivot:
        #             e -= 1
        #     # print(nums)

        #     return quickSort(nums[:s]) + [pivot] + quickSort(nums[s:])

        # 快排取中值2
        # def quickSort(nums, start, end):
        #     if end - start < 1:
        #         return
        #     # m可取数列中任意数，此处取中位
        #     s, m, e = start, start + end >> 1, end
        #     while s <= e:
        #         # 取值判定加等号，防止nums[m]值被交换
        #         while s <= e and  nums[s] <= nums[m]:
        #             s += 1

        #         while s <= e and nums[e] > nums[m]:
        #             e -= 1
        #         if s < e:
        #             nums[s], nums[e] = nums[e], nums[s]
        #     if m > s:
        #         # 将nums[m]放在正确的位置
        #         nums[s], nums[m] = nums[m], nums[s]
        #         # 移动位置，缩减nums[m]位置，防止某些情况死循环（如所有值一致）
        #         s += 1
        #     else:
        #         nums[e], nums[m] = nums[m], nums[e]
        #         e -= 1

        #     if start < e:
        #         quickSort(nums, start, e)
        #     if s < end:
        #         quickSort(nums, s, end)

        # 双路快排
        def quickSort(nums, start, end):
            if end - start < 1:
                return
            s, m, e = start + 1, start, end
            while s <= e:
                while s <= e and  nums[s] < nums[m]:
                    s += 1
                while s <= e and nums[e] >= nums[m]:
                    e -= 1
                if s < e:
                    nums[s], nums[e] = nums[e], nums[s]

            nums[e], nums[m] = nums[m], nums[e]
            if start < e:
                quickSort(nums, start, e - 1)
            if s < end:
                quickSort(nums, s, end)

        # //三路快排分为下面这三个路(区间)
        # int i = left; // left表示，[lleft...left) 左闭右开区间里的数都比base小
        # int j = right;// left表示，(rright...right] 左开右闭区间里的数都比base大
        # int cur = i;//用cur来遍历数组。[left...cur)左闭右开区间里的数都等于base

        # while (cur <= j) {
        #     if (arr[cur].compareTo(base) == 0) {
        #         cur++;
        #     } else if (arr[cur].compareTo(base) < 0) {
        #         swap(arr, cur++, i++);
        #     } else {
        #         swap(arr, cur, j--);
        #     }
        # }
        #
        # def quickSort(nums, start, end):
        #     if end - start < 1:
        #         return
        #     s, c, m, e = start + 1, start + 1, start, end
        #     while c <= e:
        #         if nums[c] == nums[m]:
        #             c += 1
        #         elif nums[c] < nums[m]:
        #             nums[s], nums[c] = nums[c], nums[s]
        #             s += 1
        #             c += 1
        #         else:
        #             nums[e], nums[c] = nums[c], nums[e]
        #             e -= 1
        #     nums[e], nums[m] = nums[m], nums[e]
        #     if start < e:
        #         quickSort(nums, start, e - 1)
        #     if s < end:
        #         quickSort(nums, s, end)

        def shellSort(nums):
            span = l = len(nums)
            while span > 1:
                span //= 2
                insertionSort(nums, span)
            return nums

        def insertionSort(nums, span):
            for i in range(span, len(nums), 1):
                if nums[i] < nums[i - span]:
                    j = i - span
                    aim = nums[i]
                    while aim < nums[j] and j > -1:
                        nums[j + span] = nums[j]
                        j -= span
                    nums[j + span] = aim
            # return nums

        def biS(n, nums):
            s, m, e = 0, 0, len(nums) - 1
            # print(s, m, e)
            while s < e:
                m = s + e + 1 >> 1

                if nums[m] == n:
                    return True

                elif nums[m] > n:
                    e = m - 1
                else:
                    s = m
            return nums[e] == n
        nums3 = []
        dict = {}
        quickSort(nums2,0 ,len(nums2) - 1)
        snums2 = nums2
        # snums2 = quickSort(nums2)

        for n in nums1:
            if biS(n, snums2):
                if n not in dict:
                    nums3.append(n)
                dict[n] = True

        return nums3
# @lc code=end

# set法

# class Solution:
#     def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
#         set1 = set(nums1)
#         set2 = set(nums2)
#         return self.set_intersection(set1, set2)

#     def set_intersection(self, set1, set2):
#         if len(set1) > len(set2):
#             return self.set_intersection(set2, set1)
#         return [x for x in set1 if x in set2]


# 作者：LeetCode-Solution
# 链接：https: // leetcode-cn.com/problems/intersection-of-two-arrays/solution/liang-ge-shu-zu-de-jiao-ji-by-leetcode-solution/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


# 排序+双指针
# class Solution:
#     def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
#         nums1.sort()
#         nums2.sort()
#         length1, length2 = len(nums1), len(nums2)
#         intersection = list()
#         index1 = index2 = 0
#         while index1 < length1 and index2 < length2:
#             num1 = nums1[index1]
#             num2 = nums2[index2]
#             if num1 == num2:
#                 # 保证加入元素的唯一性
#                 if not intersection or num1 != intersection[-1]:
#                     intersection.append(num1)
#                 index1 += 1
#                 index2 += 1
#             elif num1 < num2:
#                 index1 += 1
#             else:
#                 index2 += 1
#         return intersection


# 作者：LeetCode-Solution
# 链接：https: // leetcode-cn.com/problems/intersection-of-two-arrays/solution/liang-ge-shu-zu-de-jiao-ji-by-leetcode-solution/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
