from typing import Optional

valid_opening = {
    "[": "]",
    "(": ")",
    "{": "}",
}


class Solution:
    def isValid(self, s: str) -> bool:
        index = 0
        expected: list[str] = []

        while index < len(s):
            char = s[index]
            if char in valid_opening:
                expected.append(valid_opening[char])
            else:
                try:
                    current_expected = expected.pop()
                    if current_expected != char:
                        return False
                except IndexError:
                    return False
            index = index + 1

        return len(expected) == 0


sol = Solution()

print(sol.isValid("()"))
print(sol.isValid("()[]{}"))
print(sol.isValid("(]"))
print(sol.isValid("([])"))
print(sol.isValid("([]"))
