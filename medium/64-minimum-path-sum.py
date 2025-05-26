from typing import Union


class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        cols = len(grid[0])
        rows = len(grid)

        self.cur_min = 999_999
        self.map: list[list[Union[int, None]]] = [
            [None for _ in range(cols)] for x in range(rows)
        ]

        def progress(col: int, row: int, total: int) -> int:
            if self.cur_min < total:
                return total

            found_from_map = self.map[row][col]
            if found_from_map:
                return found_from_map

            if col == cols - 1 and row == rows - 1:
                res = total + grid[row][col]
                self.cur_min = min(res, self.cur_min)

                return res

            directions: list[int] = []
            if row + 1 < rows:
                directions.append(progress(col, row + 1, total + grid[row][col]))
            if col + 1 < cols:
                directions.append(progress(col + 1, row, total + grid[row][col]))
            res = min(directions if len(directions) > 0 else [0])
            self.map[row][col] = res
            return res

        return progress(0, 0, 0)


sol = Solution()


def run(grid: list[list[int]], expected: int):
    print(f"{sol.minPathSum(grid)}, expected: {expected}")


run([[1, 3, 1], [1, 5, 1], [4, 2, 1]], 7)
run([[1, 2, 3], [4, 5, 6]], 12)
run([[0]], 0)
run([[1]], 1)
run(
    [
        [7, 1, 3, 5, 8, 9, 9, 2, 1, 9, 0, 8, 3, 1, 6, 6, 9, 5],
        [9, 5, 9, 4, 0, 4, 8, 8, 9, 5, 7, 3, 6, 6, 6, 9, 1, 6],
        [8, 2, 9, 1, 3, 1, 9, 7, 2, 5, 3, 1, 2, 4, 8, 2, 8, 8],
        [6, 7, 9, 8, 4, 8, 3, 0, 4, 0, 9, 6, 6, 0, 0, 5, 1, 4],
        [7, 1, 3, 1, 8, 8, 3, 1, 2, 1, 5, 0, 2, 1, 9, 1, 1, 4],
        [9, 5, 4, 3, 5, 6, 1, 3, 6, 4, 9, 7, 0, 8, 0, 3, 9, 9],
        [1, 4, 2, 5, 8, 7, 7, 0, 0, 7, 1, 2, 1, 2, 7, 7, 7, 4],
        [3, 9, 7, 9, 5, 8, 9, 5, 6, 9, 8, 8, 0, 1, 4, 2, 8, 2],
        [1, 5, 2, 2, 2, 5, 6, 3, 9, 3, 1, 7, 9, 6, 8, 6, 8, 3],
        [5, 7, 8, 3, 8, 8, 3, 9, 9, 8, 1, 9, 2, 5, 4, 7, 7, 7],
        [2, 3, 2, 4, 8, 5, 1, 7, 2, 9, 5, 2, 4, 2, 9, 2, 8, 7],
        [0, 1, 6, 1, 1, 0, 0, 6, 5, 4, 3, 4, 3, 7, 9, 6, 1, 9],
    ],
    85,
)
