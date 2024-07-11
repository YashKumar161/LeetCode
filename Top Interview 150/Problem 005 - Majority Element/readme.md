# Majority Element

## Problem Name
Majority Element

## Approach
Finding the Majority Element (majorityElement method):
-The majorityElement method finds the element that appears more than n // 2 times in the input array nums.
-It uses a dictionary (m) to count occurrences of each element.

## Problem Link
[Majority Element](https://leetcode.com/problems/majority-element/description/?envType=study-plan-v2&envId=top-interview-150)

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

