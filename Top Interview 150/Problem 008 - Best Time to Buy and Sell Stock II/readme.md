# Best Time to Buy and Sell Stock II

## Problem Name
Best Time to Buy and Sell Stock II

## Approach
Max Profit from Stock Prices II (maxProfit method):
-Initialize max to 0 to keep track of the maximum profit and start with the first price.
-Iterate over the prices.
-If the current price is higher than start, add the difference to max (indicating a sell at the current price and buy at start).
-Update start to the current price.
-Return the accumulated max profit after the loop ends.

## Problem Link
[Best Time to Buy and Sell Stock II](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/?envType=study-plan-v2&envId=top-interview-150)

## Credits
Solved by: Yash Kumar

- Email: imrja8@gmail.com
- Professional Email: hello@yashkumar.pro
- Website: [https://www.yashkumar.pro](https://www.yashkumar.pro)
- LinkedIn: [https://www.linkedin.com/in/yash-kumar-talan/](https://www.linkedin.com/in/yash-kumar-talan/)

## Solution
```python
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max = 0
        start = prices[0]
        len1 = len(prices)
        for i in range(0 , len1):
            if start < prices[i]: 
                max += prices[i] - start
            start = prices[i]
        return max