class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        Counts = [0,0,0]

        for Color in nums:
            Counts[Color] += 1

        R, W, B = Counts
        nums[:R] = [0] * R
        nums[R:R+W] = [1] * W
        nums[R+W:] = [2] * B

        #Time : O(n)
        #Space: O(1)