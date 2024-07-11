# Rotate Array

## Problem Name
Rotate Array

## Approach
Rotating an Array (rotate method):
-First, we calculate the effective number of rotations needed by taking k % len(nums) because rotating the array len(nums) times results in the same array.
-Next, we determine the number of elements to move from the end to the beginning (r), which is len(nums) - k.
-We then store the first r elements in a new list new.
-We remove these elements from the original list.
-Finally, we append the stored elements to the end of the modified list.

## Problem Link
[Rotate Array](https://leetcode.com/problems/rotate-array/description/?envType=study-plan-v2&envId=top-interview-150)

## Credits
Solved by: Yash Kumar

- Email: imrja8@gmail.com
- Professional Email: hello@yashkumar.pro
- Website: [https://www.yashkumar.pro](https://www.yashkumar.pro)
- LinkedIn: [https://www.linkedin.com/in/yash-kumar-talan/](https://www.linkedin.com/in/yash-kumar-talan/)

## Solution
```python
class Solution(object):
   def rotate(self, nums, k):
       # Get the actual number of rotations
       k = k % len(nums)      
       # Get the number of elements to move from the end to the beginning
       r = len(nums) - k
       # Store the elements to move
       new = nums[0:r]
       # Remove the elements from the beginning
       nums[0:r] = []
       # Append the stored elements to the end
       nums.extend(new)
