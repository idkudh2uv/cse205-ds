class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        minVal, maxVal = min(nums), max(nums)
        for n in nums:
            if n != minVal and n != maxVal:
                return n
        return -1