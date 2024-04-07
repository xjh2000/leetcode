#
# @lc app=leetcode.cn id=70 lang=python3
#
# [70] 爬楼梯
#


# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        return self.solve(n)

    def solve(self, n: int) -> int:
        if n == 0:
            return 1
        count = 0
        if n >= 2:
            count += self.solve(n - 2)
        if n >= 1:
            count += self.solve(n - 1)
        return count


# @lc code=end
