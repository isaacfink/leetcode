class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min_price = prices[0]
        res = 0
        for price in prices[1:]:
            res = max(res, price - min_price)
            min_price = min(min_price, price)
        return res


sol = Solution()
print(sol.maxProfit([7, 1, 5, 3, 6, 4]))  # Expected 5
print(sol.maxProfit([7, 6, 4, 3, 1]))  # Expected 0
