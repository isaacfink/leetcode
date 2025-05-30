from typing import Union


class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.removeprefix("0")
        print(s)

        return int(s)


sol = Solution()

print(sol.myAtoi("0000000-42"))  # Expected: 42
