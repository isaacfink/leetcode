class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        index = 0

        while index < len(nums1) and len(nums2) > 0:
            v1, v2 = nums1[index], nums2[0]
            if v2 < v1:
                nums1.insert(index, v2)
                del nums2[0]
            else:
                index += 1
        nums1[m + n - len(nums2) : len(nums1)] = nums2


# [1,2,3,0,0,0], [2,5,6]

sol = Solution()

nums1 = [1, 2, 3, 0, 0, 0]
sol.merge(nums1=nums1, nums2=[2, 5, 6], n=3, m=3)
print(nums1)  # Expected: [1,2,2,3,5,6]

nums1 = [1]
sol.merge(nums1=nums1, nums2=[], n=0, m=1)
print(nums1)  # Expected: [1]

nums1 = [0]
sol.merge(nums1=nums1, nums2=[1], n=1, m=0)
print(nums1)  # Expected: [1]

nums1 = [4, 0, 0, 0, 0, 0]
sol.merge(nums1=nums1, nums2=[1, 2, 3, 5, 6], n=5, m=1)
print(nums1)  # Expected: [1,2,3,4,5,6]
