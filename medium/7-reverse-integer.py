class Solution:
    def reverse(self, x: int) -> int:
        range_min, range_max = -2147483648, 2147483647
        s = "-" if x < 0 else ""
        res = int(s + "".join(list(reversed(str(x).removeprefix("-")))))
        if res < range_min or res > range_max:
            return 0
        return res


sol = Solution()

print(sol.reverse(123))  # expected 321
