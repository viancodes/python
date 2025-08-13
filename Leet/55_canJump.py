class Solution:
    def canJump(self, nums):
        far = 0
        for i, step in enumerate(nums):
            if i > far:
                return False
            far = max(far, i + step)
            if far >= len(nums) - 1:
                return True
        return True
