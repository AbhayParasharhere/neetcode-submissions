class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        n = len(arr)
        if n < 2: return 1
        dp = [[0,0] for _ in range(n)]

        dp[0] = [1,1]

        # dp at i represents the max trubulent array size at i
        # dp[i][0] val means the current run max size in the up direction - it needs down or les value next time to extend furtehr or reset back to 1
        # dp[i][1] val means the current run max size in the down durection - it needs up value next time to extend furtehr 

        best = 1

        for i in range(1,n):
            if arr[i] == arr[i-1]:
                dp[i][0] = 1
                dp[i][1] = 1
            elif arr[i] > arr[i-1]:
                # extends teh best answer in teh previous down chain
                dp[i][0] = dp[i-1][1] + 1
                # resets the up chain
                dp[i][1] = 1
            elif arr[i] < arr[i-1]:
                dp[i][0] = 1
                dp[i][1] = dp[i-1][0] + 1
            best = max(dp[i][0],dp[i][1],best)
        return best
