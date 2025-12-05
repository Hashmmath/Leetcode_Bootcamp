class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        target, remainder = divmod(total_sum, 2)
      
        if remainder != 0:
            return False
      
        n = len(nums)
      
        dp = [[False] * (target + 1) for _ in range(n + 1)]
      
        dp[0][0] = True
      
        for i in range(1, n + 1):
            current_num = nums[i - 1]  
          
            for j in range(target + 1):
                dp[i][j] = dp[i - 1][j]  
              
                if j >= current_num:  
                    dp[i][j] = dp[i][j] or dp[i - 1][j - current_num]
      
        return dp[n][target]