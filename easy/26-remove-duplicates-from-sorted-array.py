class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        index = 0
        while index < len(nums) - 1:
            while True:
                if index == len(nums) - 1:
                    break
                if nums[index] == nums[index + 1]:
                    del nums[index + 1]
                else:
                    break
            index += 1

        return len(nums)


sol = Solution()

nums1 = [1, 1, 2]
print(sol.removeDuplicates(nums1))  # expected: 2, nums = [1,2,_]
print(nums1)

nums2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
print(sol.removeDuplicates(nums2))  # expected: 5, nums = [0,1,2,3,4,_,_,_,_,_]
print(nums2)

nums3 = [1, 1]
print(sol.removeDuplicates(nums3))  # expected: 1, nums = [1, _]
print(nums3)

nums4 = [0, 0, 0, 0, 3, 4]
print(sol.removeDuplicates(nums4))  # expected: 3, nums = [0,3,4,_,_,_]
print(nums4)
