class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            res += n & 0b0000000000001
            n = n >> 1
        return res

    def countBits(self, n: int) -> list[int]:
        return [self.hammingWeight(x) for x in range(n + 1)]


sol = Solution()

print(sol.countBits(2))  # Expected: [0,1,1]
print(sol.countBits(5))  # Expected: [0,1,1,2,1,2]
