# Dynamic Programming

<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [Dynamic Programming](#dynamic-programming)
  - [概述](#概述)
    - [常见类型](#常见类型)
    - [解题思路](#解题思路)
  - [子序列问题](#子序列问题)
    - [问题描述](#问题描述)
    - [解题思路](#解题思路-1)
  - [背包问题](#背包问题)
    - [问题特征](#问题特征)
    - [背包问题状态转移方程](#背包问题状态转移方程)
  - [实战](#实战)
    - [最大公共子串](#最大公共子串)
    - [一步两步爬楼梯](#一步两步爬楼梯)
  - [BMW WARNING](#bmw-warning)
    - [Bulletin](#bulletin)
    - [Material](#material)
    - [Warrant](#warrant)

<!-- /code_chunk_output -->

## 概述

### 常见类型

![Dynamic_ProgrammingUntitled](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/Dynamic_ProgrammingUntitled.png)
| Name | Leetcode Problems |
| --- | --- |
| 基本动态规划: 一维 | 70 |
| 基本动态规划:二维 | 64，403 |
| 分割类型题 | |
| 子序列问题 | 5 |
| 背包问题 | 322，416 |
| 字符串编辑 | |
| 股票交易 | |

### 解题思路

![Dynamic_ProgrammingUntitled 1](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/Dynamic_ProgrammingUntitled%201.png)

## 子序列问题

### 问题描述

对于子序列涉及的遍历

通常情况下，遍历子串或者子序列有三种方式
以[a, b , c, d , e]为例子

### 解题思路

- 节点开头

以某个节点为开头

如 [a]，[a, b]，[ a, b, c] ... 再从以 b 为开头的子序列开始遍历 [b] [b, c]
常用于暴力解法

- 长度标杆

以子序列的长度为标杆

先遍历出子序列长度为 1 的子序列，在遍历出长度为 2 的 等等
leetcode (5. 最长回文子串 ) 中的解法就用到了。

- 基准尾节点

以子序列的结束节点为基准

以 b 为结束点的所有子序列: [a , b] [b] 以 c 为结束点的所有子序列: [a, b, c] [b, c] [ c ]
这种方式可以产生递推关系, 采用动态规划时, 经常通过此种遍历方式。如背包问题, 最大公共子串。

## 背包问题

### 问题特征

有一个明确的目标值，从一堆值中取出部分值和是否可得到目标值

| Name                   | Feature          | Template                                                           | Problems |
| ---------------------- | ---------------- | ------------------------------------------------------------------ | -------- |
| 0/1 背包问题           | 元素最多选取一次 | 外循环遍历 arrs，内循环遍历 target，且内循环倒序                   | 422，494 |
| 完全背包问题(顺序无关) | 元素可以重复选择 | arrs 放在外循环（保证 arrs 按顺序），target 在内循环。且内循环正序 | 322      |

| 完全背包问题(顺序有关)
[即 组合背包问题] | 元素可以重复选择 | 如果组合问题需考虑元素之间的顺序，需将 target 放在外循环，将 arrs 放在内循环，且内循环正序 | 377 |
| 分组背包问题 | 不止一个背包，需要遍历每个背包 | 需要 3+层循环 | 474 |

### 背包问题状态转移方程

| Name                 | Formula                    | Problems                 |
| -------------------- | -------------------------- | ------------------------ | ------- |
| 组合背包问题         | dp[i] += dp[i-num]         | 377 494 518              |
| True、False 问题公式 | dp[i] = dp[i] or dp[i-num] | 139 416                  |
| 最值问题             | dp[i] = min                | max(dp[i], dp[i-num]+1)) | 322 474 |

## 实战

### 最大子串

- 描述

> Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

- 基本思路

这里的动态规划解法也是以先遍历出以**某个节点为结束节点**的最大子序列的思路，并以备忘录来记录最大值减少空间消耗。

- 状态转移方程

在 n = [a, b , c, d , e]这个数组中，以 c 结尾的最大子序列为 dp[2]，当继续遍历到以 d 结尾时，dp[3]的大小取决于 dp[2] + d 与 d 的大小，由此可以得出状态转移方程
`dp[i] = max(dp[i - 1) + n[i], n[i])`

- 题解

```jsx
/**
 * @param {number[]} nums
 * @return {number}
 */
var maxSubArray = function (nums) {
  let sum = nums[0]
  let ret = nums[0] // 备忘录
  for (let i = 1; i < nums.length; i++) {
    // 注意边界情况，从1开始
    sum = Math.max(sum + nums[i], nums[i]) // 状态转移方程
    ret = Math.max(ret, sum)
  }
  return ret
}

var maxSubArray = function (nums) {
  let ret = nums[0]
  let sum = 0
  for (let num of nums) {
    // if(sum > 0) { 可以写成这样
    if (sum + num > num) {
      sum = sum + num
    } else {
      sum = num
    }
    ret = Math.max(ret, sum)
  }
  return ret
}
```

### 一步两步爬楼梯

- 描述

You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

- DP 解法

状态转移方程
`dp[n] = dp[n - 1] + dp[n - 2]`

```jsx
/**
 * @param {number} n
 * @return {number}
 */
var climbStairs = function (n) {
  let pre = 1
  let next = 1
  for (let i = 1; i < n; i++) {
    let temp = next
    next = next + pre
    pre = temp
  }

  return next
}

// dp[n] 到达第n阶的方案总数
// dp[n] = dp[n - 1] + dp[n - 2]
```

- 递归解法

在动态规划中，我们看到，状态转移方程是典型的斐波那契函数

```jsx
var climbStairs = function (n) {
  const recursion = (n) => {
    if (n <= 2) return n
    return recursion(n - 1) + recursion(n - 2)
  }
  return recursion(n)
}
```

## BMW WARNING

### Bulletin

本文首发于 [skyline.show](skyline.show) 欢迎访问。

> I am a bucolic migrant worker but I never walk backwards.

### Material

参考资料如下列出，部分引用可能遗漏或不可考，侵删。

>

### Warrant

本文作者： Skyline(lty)
授权声明： 本博客所有文章除特别声明外， 均采用 CC BY - NC - SA 3.0 协议。 转载请注明出处！

> [CC BY - NC - SA 3.0](https://creativecommons.org/licenses/by-nc-sa/3.0/deed.zh)
