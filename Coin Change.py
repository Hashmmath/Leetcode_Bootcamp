class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        num_coins = len(coins)
      
        dp = [[float('inf')] * (amount + 1) for _ in range(num_coins + 1)]
      
        dp[0][0] = 0
      
        for coin_idx in range(1, num_coins + 1):
            current_coin_value = coins[coin_idx - 1]
          
            for current_amount in range(amount + 1):
                dp[coin_idx][current_amount] = dp[coin_idx - 1][current_amount]
              
                if current_amount >= current_coin_value:
                    dp[coin_idx][current_amount] = min(
                        dp[coin_idx][current_amount],
                        dp[coin_idx][current_amount - current_coin_value] + 1
                    )
        return -1 if dp[num_coins][amount] == float('inf') else dp[num_coins][amount]