# Gas Station

## Problem Name
Gas Station

## Approach
-Calculate the total gas and total cost. If the total cost is greater than the total gas, return -1 as it's impossible to complete the circuit.
-Initialize current_gas to track the gas available and starting_index to determine the start point.
-Iterate through the gas stations, updating the current_gas by subtracting the cost from the gas at each station.
-If current_gas becomes negative, reset it to 0 and update the starting_index to the next station.
-Return the starting_index after the loop ends.

## Problem Link
[Gas Station](https://leetcode.com/problems/gas-station/description/?envType=study-plan-v2&envId=top-interview-150)

## Credits
Solved by: Yash Kumar

- Email: imrja8@gmail.com
- Professional Email: hello@yashkumar.pro
- Website: [https://www.yashkumar.pro](https://www.yashkumar.pro)
- LinkedIn: [https://www.linkedin.com/in/yash-kumar-talan/](https://www.linkedin.com/in/yash-kumar-talan/)

## Solution
```python
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        sum_cost = sum(cost)
        sum_gas = sum(gas)
        
        if sum_cost > sum_gas:
            return -1

        current_gas = 0
        starting_index = 0

        for i in range(len(gas)):
            current_gas += gas[i] - cost[i]
            if current_gas < 0:
                current_gas = 0
                starting_index = i + 1
        return starting_index
