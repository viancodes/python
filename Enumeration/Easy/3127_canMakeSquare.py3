class Solution:
    def canMakeSquare(self, grid) -> bool:
        for i in range(2):
            for j in range(2):
                block = [
                    grid[i][j], grid[i][j+1],
                    grid[i+1][j], grid[i+1][j+1]
                ]
                countB = block.count("B")
                countW = 4 - countB
                if countB == 4 or countW == 4:  # already uniform
                    return True
                if countB == 3 or countW == 3:  # flip one cell
                    return True
        return False
