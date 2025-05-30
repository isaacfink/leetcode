class Solution:
    def reverseBits(self, n: int) -> int:
        return int("".join(list(reversed("{:b}".format(n).rjust(32, "0")))), 2)


sol = Solution()

print(
    sol.reverseBits(0b00000010100101000001111010011100)
)  # Expected: 964176192 (00111001011110000010100101000000)
print(sol.reverseBits(0b11111111111111111111111111111101))  # Expected: 3221225471
