# Jump Game

## Problem Name
Jump Game

## Approach
Jump Game (jump method):
-Initialize gas to 0, representing the maximum number of steps we can take.
-Iterate through each number in the list.
-If gas is less than 0 at any point, return False (indicating we can't reach the end).
-Update gas to the current number if it's greater than gas.
-Decrease gas by 1 for each step taken.
-Return True if we successfully iterate through the list without gas dropping below 0.

## Problem Link
[Jump Game](https://leetcode.com/problems/jump-game/description/?envType=study-plan-v2&envId=top-interview-150)

## Credits
Solved by: Yash Kumar

- Email: imrja8@gmail.com
- Professional Email: hello@yashkumar.pro
- Website: [https://www.yashkumar.pro](https://www.yashkumar.pro)
- LinkedIn: [https://www.linkedin.com/in/yash-kumar-talan/](https://www.linkedin.com/in/yash-kumar-talan/)

## Solution
```python
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        gas = 0
        for n in nums:
            if gas < 0:
                return False
            elif n > gas:
                gas = n
            gas -= 1
            
        return True