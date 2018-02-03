class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) <= 1:
            return 0
        minPrices = prices[0]
        ans = 0
        for i in range(1, len(prices)):
            if prices[i] < minPrices:
                minPrices = prices[i]
            elif prices[i] - minPrices >= ans:
                ans = prices[i] - minPrices
        return ans


if __name__ == '__main__':
    s = Solution()
    prices = [7, 2, 5, 4, 1, 3]
    print(s.maxProfit(prices))
