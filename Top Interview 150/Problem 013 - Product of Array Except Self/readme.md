# Product of Array Except Self

## Problem Name
Product of Array Except Self

## Approach
-Calculate the prefix product array, where prefix[i] is the product of all elements before index i.
-Calculate the suffix product array, where suffix[i] is the product of all elements after index i.
-For each element in nums, the product of all elements except itself is the product of the corresponding prefix and suffix elements.
-Handle the boundary conditions separately for the first and last elements.

## Problem Link
[Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/description/?envType=study-plan-v2&envId=top-interview-150)

## Credits
Solved by: Yash Kumar

- Email: imrja8@gmail.com
- Professional Email: hello@yashkumar.pro
- Website: [https://www.yashkumar.pro](https://www.yashkumar.pro)
- LinkedIn: [https://www.linkedin.com/in/yash-kumar-talan/](https://www.linkedin.com/in/yash-kumar-talan/)

## Solution
```python
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        prefix, suffix = list(accumulate(nums, operator.mul)), list(accumulate(reversed(nums), operator.mul))[::-1]
        for i in range(len(nums)): 
            if 0 < i < len(nums) - 1:
                output.append(prefix[i - 1] * suffix[i + 1])
            elif i == 0: 
                output.append(suffix[i + 1])
            else:
                output.append(prefix[i - 1])
        return output
