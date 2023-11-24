class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        res = []
        min_diff_so_far = float('inf')
        for val0, val1 in zip(arr, arr[1:]):
            diff = val1 - val0
            if diff < min_diff_so_far:
                min_diff_so_far = diff
                res = [(val0, val1)]
            elif diff == min_diff_so_far:
                res.append((val0, val1))
            
        return res