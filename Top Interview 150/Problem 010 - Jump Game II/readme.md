# Jump Game II

## Problem Name
Jump Game II

## Approach
Jump Game II (jump method):
-Initialize ans, end, and farthest to 0. ans keeps track of the number of jumps.
-Iterate through the list, excluding the last element.
-For each index, update farthest to the maximum value between the current farthest and i + nums[i].
-If farthest reaches or exceeds the last index, increment ans and break the loop.
-If the current index i reaches end, increment ans and update end to farthest (indicating the level is completed and the next level starts).
-Return ans as the minimum number of jumps required.


## Problem Link
[Jump Game II](https://leetcode.com/problems/jump-game-ii/description/?envType=study-plan-v2&envId=top-interview-150)

## Credits
Solved by: Yash Kumar

- Email: imrja8@gmail.com
- Professional Email: hello@yashkumar.pro
- Website: [https://www.yashkumar.pro](https://www.yashkumar.pro)
- LinkedIn: [https://www.linkedin.com/in/yash-kumar-talan/](https://www.linkedin.com/in/yash-kumar-talan/)

## Solution
```python
class Solution:
  def jump(self, nums: List[int]) -> int:
    ans = 0
    end = 0
    farthest = 0

    # Implicit BFS
    for i in range(len(nums) - 1):
      farthest = max(farthest, i + nums[i])
      if farthest >= len(nums) - 1:
        ans += 1
        break
      if i == end:      # Visited all the items on the current level
        ans += 1        # Increment the level
        end = farthest  # Make the queue size for the next level

    return ans