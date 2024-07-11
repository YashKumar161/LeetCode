# Merge Sorted Array

## Problem Name
Merge Sorted Array

## Approach
Merging Two Sorted Arrays (merge method):
-The merge method takes two sorted arrays, nums1 and nums2, along with their respective lengths (m and n).
-It appends the elements from nums2 into nums1 starting from index m.
-Finally, it sorts the combined array nums1.

## Problem Link
[Merge Sorted Array](https://leetcode.com/problems/merge-sorted-array/?envType=study-plan-v2&envId=top-interview-150)

## Credits
Solved by: Yash Kumar

- Email: imrja8@gmail.com
- Professional Email: hello@yashkumar.pro
- Website: [https://www.yashkumar.pro](https://www.yashkumar.pro)
- LinkedIn: [https://www.linkedin.com/in/yash-kumar-talan/](https://www.linkedin.com/in/yash-kumar-talan/)

## Solution
```python
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        for j in range(n):
            nums1[m+j] = nums2[j]
        nums1.sort()
