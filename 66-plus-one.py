class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        index = 1
        while True:
            if index > len(digits):
                return [1] + digits
            digits[-index] = digits[-index] + 1
            if digits[-index] < 10:
                break
            else:
                digits[-index] = digits[-index] % 10
            index = index + 1
        return digits
        # first solution, o(n)
        # return [int(x) for x in str(int("".join([str(j) for j in digits])) + 1)]


sol = Solution()


def run(l: list[int], expected: list[int]):
    print(f"{sol.plusOne(l)}, expected: {expected}")


run([1, 2, 3], [1, 2, 4])
run([4, 3, 2, 1], [4, 3, 2, 2])
run([9], [1, 0])
