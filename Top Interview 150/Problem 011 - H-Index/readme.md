# H-Index

## Problem Name
H-Index

## Approach
-First, sort the citations list.
-Iterate through the sorted list with both the index (i) and the value (v).
-For each citation, check if the number of papers with at least that many citations (n - i) is less than or equal to the citation count (v).
-If the condition is met, return n - i as the H-Index.
-If no such index is found, return 0.

## Problem Link
[H-Index](https://leetcode.com/problems/h-index/description/?envType=study-plan-v2&envId=top-interview-150)

## Credits
Solved by: Yash Kumar

- Email: imrja8@gmail.com
- Professional Email: hello@yashkumar.pro
- Website: [https://www.yashkumar.pro](https://www.yashkumar.pro)
- LinkedIn: [https://www.linkedin.com/in/yash-kumar-talan/](https://www.linkedin.com/in/yash-kumar-talan/)

## Solution
```python
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        citations.sort()

        for i, v in enumerate(citations):
            if n - i <= v:
                return n - i
        return 0
