class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        left = 0
        right = left + 1
        N = len(prices)

        while right < N:
            if prices[right] < prices[left]:
                left = right

            else:
                maxProfit = max(maxProfit,prices[right]-prices[left])
            
            
            right+=1

        return maxProfit
