# Candy

## Problem Name
Candy

## Approach
-Initialize the candies list with 1 candy for each child.
-Perform a left-to-right pass to ensure that each child has more candies than the left neighbor if their rating is higher.
-Perform a right-to-left pass to ensure that each child has more candies than the right neighbor if their rating is higher, taking the maximum between the current value and candies[i+1] + 1.
-Return the sum of the candies list as the minimum number of candies required.
## Problem Link
[Candy](https://leetcode.com/problems/candy/description/?envType=study-plan-v2&envId=top-interview-150)

## Credits
Solved by: Yash Kumar

- Email: imrja8@gmail.com
- Professional Email: hello@yashkumar.pro
- Website: [https://www.yashkumar.pro](https://www.yashkumar.pro)
- LinkedIn: [https://www.linkedin.com/in/yash-kumar-talan/](https://www.linkedin.com/in/yash-kumar-talan/)

## Solution
```python
from typing import List
from collections import defaultdict

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        m = defaultdict(int)

        for num in nums:
            m[num] += 1

        threshold = n // 2
        for key, value in m.items():
            if value > threshold:
                return key

        return 0

