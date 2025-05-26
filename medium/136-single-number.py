class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        res = 0
        for num in nums:
            res = res ^ num
        return res


sol = Solution()
print(sol.singleNumber([2, 2, 1]))  # expected: 1
print(sol.singleNumber([4, 1, 2, 1, 2]))  # expected: 4
print(sol.singleNumber([1]))  # expected: 1
