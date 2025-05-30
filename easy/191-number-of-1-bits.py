class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            res += n & 0b0000000000001
            n = n >> 1
        return res


sol = Solution()
print(sol.hammingWeight(11))  # Expected: 3
print(sol.hammingWeight(128))  # Expected: 1
print(sol.hammingWeight(2147483645))  # Expected: 30
