class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        return len(list(set(nums))) != len(nums)


sol = Solution()

print(sol.containsDuplicate([1, 2, 3, 1]))  # Expected: True
print(sol.containsDuplicate([1, 2, 3, 4]))  # Expected: False
print(sol.containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))  # Expected: True
