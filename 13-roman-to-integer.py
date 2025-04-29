lookup_map = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
}


class Solution:
    def romanToInt(self, s: str) -> int:
        total = 0

        lhp = 0
        rhp = 1
        lhv = lookup_map[s[lhp]]
        while rhp <= len(s):
            if rhp == len(s):
                total = total + lhv
                break
            rhv = lookup_map[s[rhp]]
            if lhv >= rhv:
                total = total + lhv
                lhv = rhv
                lhp = lhp + 1
                rhp = rhp + 1
            else:
                lhv = rhv - lhv
                lhp = lhp + 1
                rhp = rhp + 1

        return total
