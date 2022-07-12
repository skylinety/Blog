#
# @lc app=leetcode.cn id=1023 lang=python3
#
# [1023] 驼峰式匹配
#

# @lc code=start
class Solution:

        
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        def strMatch(query, pattern):
            lq, lp = len(query), len(pattern)
            i, j = 0, 0
            while i < lp:
                while j < lq:
                    if query[j] == pattern[i]:
                        i += 1
                        j += 1
                        break
                    if ord(query[j]) < 91:
                        return False
                    j += 1
                if j == lq and i < lp:
                    return False
            while j < lq:
                if ord(query[j]) < 91:
                    return False
                j += 1
            return True
        return list(map(strMatch, queries, [pattern] * len(queries)))


# @lc code=end

        # def strMatch(q, pattern):
        #     i = 0
        #     j = 0
        #     M = len(q)
        #     N = len(pattern)
        #     while (i < M):
        #         if (j < N and q[i] == pattern[j]):
        #             i += 1
        #             j += 1
        #         elif q[i].isupper():
        #             return False
        #         else:
        #             i += 1

        #     return i == M and j == N
