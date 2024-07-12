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
