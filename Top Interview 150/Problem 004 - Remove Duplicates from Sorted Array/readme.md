# Remove Duplicates from Sorted Array II

## Problem Name
Remove Duplicates from Sorted Array II

## Approach
Removing Duplicates (Allowing at Most Two Duplicates) (removeDuplicates method):
-This version of removeDuplicates allows at most two duplicates.
-It maintains a pointer i that skips over elements if they appear more than twice.

## Problem Link
[Remove Duplicates from Sorted Array II](https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/description/?envType=study-plan-v2&envId=top-interview-150)

## Credits
Solved by: Yash Kumar

- Email: imrja8@gmail.com
- Professional Email: hello@yashkumar.pro
- Website: [https://www.yashkumar.pro](https://www.yashkumar.pro)
- LinkedIn: [https://www.linkedin.com/in/yash-kumar-talan/](https://www.linkedin.com/in/yash-kumar-talan/)

## Solution
```python
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 2
        for j in range(2, len(nums)):
            if nums[j] > nums[i - 2]:
                nums[i] = nums[j]
                i += 1
        return i


