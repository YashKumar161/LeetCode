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