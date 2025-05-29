class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        index = 0
        while index < len(nums):
            if nums[index] == val:
                del nums[index]
            else:
                index += 1

        return len(nums)


sol = Solution()

nums1 = [3, 2, 2, 3]
print(sol.removeElement(nums=nums1, val=3))  # expected: 2
print(nums1)  # expected: [2,2,_,_]

nums2 = [0, 1, 2, 2, 3, 0, 4, 2]
print(sol.removeElement(nums=nums2, val=2))  # expected: 5
print(nums2)  # expected: [0,1,4,0,3,_,_,_]
