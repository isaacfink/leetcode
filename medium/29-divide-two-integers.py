class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == divisor:
            return 1
        if dividend == -(2**31) and divisor == -1:
            return (2**31) - 1

        if divisor == 1:
            return dividend

        sign = -1 if (dividend < 0) ^ (divisor < 0) else 1

        n, d = abs(dividend), abs(divisor)
        ans = 0

        while n >= d:
            p = 0
            while n >= (d << p):
                p += 1

            p -= 1
            n -= d << p
            ans += 1 << p

        return min(max(sign * ans, -(2**31)), 2**31 - 1)


sol = Solution()

print(sol.divide(10, 3))  # Expected: 3
print(sol.divide(7, -3))  # Expected: -2
print(sol.divide(1, 1))  # Expected: 1
print(sol.divide(-1, 1))  # Expected: -1
print(sol.divide(-1, -1))  # Expected: 1
print(sol.divide(-2147483648, -1))  # Expected: 1
