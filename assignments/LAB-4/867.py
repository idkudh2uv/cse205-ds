class Solution:
    def transpose(self, arr):
        n = len(arr)
        m = len(arr[0])

        ans = [[0] * n for _ in range(m)]

        for i in range(n):
            for j in range(m):
                ans[j][i] = arr[i][j]

        return ans