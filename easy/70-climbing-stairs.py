class Solution:
    def climbStairs(self, n: int) -> int:
        # a = prev, b = cur
        a, b = 0, 1
        for i in range(n):
            a, b = b, a + b

        return b


sol = Solution()


# test cases
print(sol.climbStairs(1))  # Expected: 1
print(sol.climbStairs(2))  # Expected: 2
print(sol.climbStairs(3))  # Expected: 3
print(sol.climbStairs(4))  # Expected: 5
print(sol.climbStairs(5))  # Expected: 8
print(sol.climbStairs(6))  # Expected: 13
print(sol.climbStairs(7))  # Expected: 21
print(sol.climbStairs(8))  # Expected: 34
print(sol.climbStairs(9))  # Expected: 55
