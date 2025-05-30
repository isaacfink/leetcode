class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        l = sorted(nums)
        for i in range(len(l)):
            if i != l[i]:
                return i
        return len(l)
