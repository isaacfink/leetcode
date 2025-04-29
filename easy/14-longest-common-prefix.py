class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        res = ""
        index = 0

        while True:
            local_res = strs[0][0:index]
            for s in strs:
                if not s[0:index] == local_res or len(s) < index:
                    break
            else:
                index = index + 1
                continue
            break

        return strs[0][0 : index - 1]


def run(s: list[str], expected: str):
    sol = Solution()
    print(f"Solving for {s}")
    print(f"{sol.longestCommonPrefix(s)}, expected: {expected}")
    print()


run(["flower", "flow", "flight"], "fl")
run(["dog", "racecar", "car"], "")
run([""], "")
