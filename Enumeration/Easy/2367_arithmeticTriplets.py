class Solution:
    def arithmeticTriplets(self, nums, diff):
        nums_set = set(nums)
        count = 0
        
        for x in nums:
            if (x + diff) in nums_set and (x + 2 * diff) in nums_set:
                count += 1
        
        return count
