from typing import Union


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        matrix: list[list[Union[str, None]]] = [
            [None for i in range(len(s))] for i in range(numRows)
        ]

        directions = [[1, 0], [-1, 1]]
        cur_dir = [0, 1]

        cur_pos = [0, 0]

        for i in s:
            matrix[cur_pos[0]][cur_pos[1]] = i
            if cur_pos[0] == 0 and numRows > 1:
                cur_dir = directions[0]
            elif cur_pos[0] == numRows - 1 and numRows > 1:
                cur_dir = directions[1]
            cur_pos = [cur_pos[0] + cur_dir[0], cur_pos[1] + cur_dir[1]]

        return "".join([x if x is not None else "" for xs in matrix for x in xs])


sol = Solution()

print(sol.convert(s="PAYPALISHIRING", numRows=3))  # Expected: PAHNAPLSIIGYIR
print(sol.convert(s="PAYPALISHIRING", numRows=4))  # Expected: PINALSIGYAHRPI
print(sol.convert(s="AB", numRows=1))  # Expected: AB
