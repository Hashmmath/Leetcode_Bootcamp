class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        L = 0
        R = n-1

        while L < R:
            Sum = numbers[L] + numbers[R]
            if target == Sum:
                return(L+1, R+1)
            elif Sum < target:
                L += 1
            else:
                R -= 1

        #Time : O(n)
        #Space: O(1)