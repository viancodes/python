class Solution:
    def incremovableSubarrayCount(self, nums):
        n = len(nums)

        def strictly_inc(arr):
            return all(arr[i] < arr[i+1] for i in range(len(arr)-1))

        res = 0
        for l in range(n):
            for r in range(l, n):
                arr = nums[:l] + nums[r+1:]
                if strictly_inc(arr):
                    res += 1
        return res
