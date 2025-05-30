class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = "".join([x for x in s if x.isalnum()])
        lh, rh = 0, len(s) - 1

        while lh < rh:
            if s[lh] != s[rh]:
                return False
            lh += 1
            rh -= 1
        return True


sol = Solution()

print(sol.isPalindrome("A man, a plan, a canal: Panama"))  # Expected: True
print(sol.isPalindrome("race a car"))  # Expected: False
print(sol.isPalindrome(" "))  # Expected: True
