class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        self.res: list[list[int]] = [[]]
        self.map = {}
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                val = nums[i : j + 1] if j < len(nums) else [nums[i]]
                if not self.map.get(str(val)):
                    self.res.append(val)
                self.map[str(val)] = True

        return self.res


sol = Solution()
# print(sol.subsetsWithDup([1, 2, 2]))  # expected: [[],[1],[1,2],[1,2,2],[2],[2,2]]
# print(sol.subsetsWithDup([0]))  # expected: [[], [0]]
print(sol.subsetsWithDup([1, 2, 3]))  # expected: [[], [0]]
