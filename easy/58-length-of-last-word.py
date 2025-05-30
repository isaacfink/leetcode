class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        rh, lh = len(s) - 1, len(s) - 1
        while s[rh] == " ":
            rh, lh = rh - 1, lh - 1
        while s[lh] != " " and lh >= 0:
            lh -= 1
        return rh - lh


sol = Solution()

print(sol.lengthOfLastWord("Hello World"))  # expected: 5
print(sol.lengthOfLastWord("   fly me   to   the moon  "))  # expected: 4
print(sol.lengthOfLastWord("luffy is still joyboy"))  # expected: 6
print(sol.lengthOfLastWord("a"))  # expected: 1
