class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort() # sort the array
        return sum(nums[::2]) # return the sum of every other element in the sorted array