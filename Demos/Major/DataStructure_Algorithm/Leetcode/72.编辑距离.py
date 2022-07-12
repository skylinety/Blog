# @before-stub-for-debug-begin
from python3problem72 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=72 lang=python3
#
# [72] 编辑距离
#

# @lc code=start
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = 0
        n = 0
        i = 1
        j = 1

        dp = [[0] * (len(word1) + 1) for _ in range(len(word2) + 1)]
        while m <= len(word1):  # 遍历字符串的第一种办法
            dp[0][m] = m
            m = m + 1
        while n <=len(word2):  # 遍历字符串的第一种办法
            dp[n][0] = n
            n = n + 1
        while i <= len(word2):
            j = 1  # 遍历字符串的第一种办法
            while j <= len(word1):
                if word1[j - 1] == word2[i - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i]
                                   [j-1], dp[i-1][j]) + 1
                j = j + 1
            i = i + 1

        return dp[-1][-1]

    # dp[i][j]=min(dp[i-1][j-1],dp[i][j-1],dp[i-1][j])+1
    # @lc code=end

    # 对“dp[i-1][j-1] 表示替换操作，dp[i-1][j] 表示删除操作，dp[i][j-1] 表示插入操作。”的补充理解：

    # 以 word1 为 "horse"，word2 为 "ros"，且 dp[5][3] 为例，即要将 word1的前 5 个字符转换为 word2的前 3 个字符，也就是将 horse 转换为 ros，因此有：

    # (1) dp[i-1][j-1]，即先将 word1 的前 4 个字符 hors 转换为 word2 的前 2 个字符 ro，然后将第五个字符 word1[4]（因为下标基数以 0 开始） 由 e 替换为 s（即替换为 word2 的第三个字符，word2[2]）

    # (2) dp[i][j-1]，即先将 word1 的前 5 个字符 horse 转换为 word2 的前 2 个字符 ro，然后在末尾补充一个 s，即插入操作

    # (3) dp[i-1][j]，即先将 word1 的前 4 个字符 hors 转换为 word2 的前 3 个字符 ros，然后删除 word1 的第 5 个字符


# class Solution:
#     def minDistance(self, word1: str, word2: str) -> int:
#         n1 = len(word1)
#         n2 = len(word2)
#         dp = [[0] * (n2 + 1) for _ in range(n1 + 1)]
#         # 第一行
#         for j in range(1, n2 + 1):
#             dp[0][j] = dp[0][j-1] + 1
#         # 第一列
#         for i in range(1, n1 + 1):
#             dp[i][0] = dp[i-1][0] + 1
#         for i in range(1, n1 + 1):
#             for j in range(1, n2 + 1):
#                 if word1[i-1] == word2[j-1]:
#                     dp[i][j] = dp[i-1][j-1]
#                 else:
#                     dp[i][j] = min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1]) + 1
#         #print(dp)
#         return dp[-1][-1]


# 作者：powcai
# 链接：https: // leetcode-cn.com/problems/edit-distance/solution/zi-di-xiang-shang-he-zi-ding-xiang-xia-by-powcai-3/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
