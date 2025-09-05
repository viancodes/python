from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        s = set(nums)
        best = 0

        for x in s:
            # only start counting at the beginning of a sequence
            if x - 1 not in s:
                length = 1
                y = x
                while y + 1 in s:
                    y += 1
                    length += 1
                if length > best:
                    best = length

        return best

