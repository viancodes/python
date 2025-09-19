class Solution:
    def maxHeightOfTriangle(self, red: int, blue: int) -> int:
        def can_build(h, red, blue):
            odd = (h + 1) // 2
            even = h // 2
            # Case 1: red starts
            red_need = odd * odd
            blue_need = even * (even + 1)
            if red >= red_need and blue >= blue_need:
                return True
            # Case 2: blue starts
            blue_need = odd * odd
            red_need = even * (even + 1)
            if red >= red_need and blue >= blue_need:
                return True
            return False

        h = 0
        while True:
            if can_build(h + 1, red, blue):
                h += 1
            else:
                break
        return h
