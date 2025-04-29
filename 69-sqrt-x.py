class Solution:
    def mySqrt(self, x: int) -> int:
        prev = 0
        while prev < x / 2 + 1:
            new_dist = (prev + 1) * (prev + 1)
            if new_dist > x:
                return prev
            else:
                prev = prev + 1
        return prev


sol = Solution()
print(sol.mySqrt(4))
print(sol.mySqrt(8))
