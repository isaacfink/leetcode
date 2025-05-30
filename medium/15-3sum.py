class Solution:

    def flip_number(self, x: int):
        if x > 0:
            return -x
        elif x < 0:
            return abs(x)
        else:
            return 0

    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res: list[list[int]] = []
        found_sets: set[str] = set()

        index = 0
        while index < len(nums) - 2:
            next_index = index + 1
            while next_index < len(nums) - 1:

                last_index = next_index + 1
                while last_index < len(nums):
                    if nums[index] + nums[next_index] + nums[last_index] == 0:
                        sorted_nums = sorted(
                            [nums[index], nums[next_index], nums[last_index]]
                        )
                        key = str([sorted_nums[0], sorted_nums[1]])
                        if key not in found_sets:
                            res.append(
                                [nums[index], nums[next_index], nums[last_index]]
                            )
                            found_sets.add(key)

                    last_index += 1
                next_index += 1
            index += 1

        return res


sol = Solution()

print(sol.threeSum([-1, 0, 1, 2, -1, -4]))  # Expected: [[-1,-1,2],[-1,0,1]]
print(sol.threeSum([0, 1, 1]))  # Expected: []
print(sol.threeSum([0, 0, 0]))  # Expected: [0, 0, 0]
print(sol.threeSum([0, 0, 0, 0]))  # Expected: [0, 0, 0]
