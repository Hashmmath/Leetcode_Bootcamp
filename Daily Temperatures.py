class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temps = temperatures
        n = len(temps)
        ans = [0] * n
        stk = []

        for i, t in enumerate(temps):
            while stk and stk[-1][0] < t:
                stk_t, stk_i = stk.pop()
                ans[stk_i] = i - stk_i

            stk.append((t, i))
        return ans

        #Time : O(n)
        #Space: O(n)