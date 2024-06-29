class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minimum = prices[0] + 1

        answer = 0

        for e in prices:
            minimum = min(e, minimum)
            answer = max(e - minimum, answer)
        
        return answer