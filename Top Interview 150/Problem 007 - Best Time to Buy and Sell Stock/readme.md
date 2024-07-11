# Best Time to Buy and Sell Stock

## Problem Name
Best Time to Buy and Sell Stock

## Approach
Max Profit from Stock Prices (maxProfit method):
-Initialize min_price with the first element and max_profit with 0.
-Iterate over the prices starting from the second element.
-For each price, update the max_profit by comparing the current max_profit with the difference between the current price and min_price.
-Update min_price with the minimum value between the current min_price and the current price.
-Return the max_profit after the loop ends.

## Problem Link
[Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/?envType=study-plan-v2&envId=top-interview-150)

## Credits
Solved by: Yash Kumar

- Email: imrja8@gmail.com
- Professional Email: hello@yashkumar.pro
- Website: [https://www.yashkumar.pro](https://www.yashkumar.pro)
- LinkedIn: [https://www.linkedin.com/in/yash-kumar-talan/](https://www.linkedin.com/in/yash-kumar-talan/)

## Solution
```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_profit = 0
        
        for price in prices[1:]:
            max_profit = max(max_profit, price - min_price)
            min_price = min(min_price, price)
            
        return max_profit