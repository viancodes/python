from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result: List[List[int]] = []

        for row_index in range(numRows):
            current_row: List[int] = []

            for col in range(row_index + 1):
                # First and last element of each row is 1
                if col == 0 or col == row_index:
                    current_row.append(1)
                else:
                    # Sum of the two numbers directly above
                    above_left = result[row_index - 1][col - 1]
                    above_right = result[row_index - 1][col]
                    current_row.append(above_left + above_right)

            result.append(current_row)

        return result
