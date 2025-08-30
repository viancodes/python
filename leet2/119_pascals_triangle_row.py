from typing import List

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row: List[int] = []
        # Initialize row with zeros
        for _ in range(rowIndex + 1):
            row.append(0)

        row[0] = 1  # first element is always 1

        for i in range(1, rowIndex + 1):
            # Update from right to left
            j = i
            while j >= 1:
                row[j] = row[j] + row[j - 1]
                j -= 1

        return row
