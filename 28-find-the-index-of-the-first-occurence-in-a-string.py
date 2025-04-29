class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        i = 0
        while i < len(haystack) - len(needle) + 1:
            if haystack[i : i + len(needle)] == needle:
                return i
            i = i + 1
        return -1


sol = Solution()


def run(hs: str, needle: str, expected: int):
    print(f"{sol.strStr(hs, needle)}, expected: {expected}")


run("sadbutsad", "sad", 0)
run("leetcode", "leeto", -1)
run("a", "a", 0)
