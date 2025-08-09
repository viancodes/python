class Solution:
    def solveSudoku(self, board):
        # Bitmask helpers
        def box_id(r, c):
            return (r // 3) * 3 + (c // 3)

        # Initialize row/col/box masks and list of empty cells
        rows = [0] * 9
        cols = [0] * 9
        boxes = [0] * 9
        empties = []

        for r in range(9):
            for c in range(9):
                ch = board[r][c]
                if ch == '.':
                    empties.append((r, c))
                else:
                    bit = 1 << (ord(ch) - ord('1'))
                    rows[r] |= bit
                    cols[c] |= bit
                    boxes[box_id(r, c)] |= bit

        ALL = (1 << 9) - 1  # 0b1_1111_1111

        def count_bits(x):
            # builtin popcount; available in Python 3.8+ via bit_count()
            return x.bit_count()

        def dfs():
            if not empties:
                return True

            # MRV: pick the empty cell with the fewest candidates
            best_i = -1
            best_mask = 0
            best_cnt = 10  # >9
            for i, (r, c) in enumerate(empties):
                mask = ALL ^ (rows[r] | cols[c] | boxes[box_id(r, c)])
                cnt = count_bits(mask)
                if cnt == 0:
                    return False
                if cnt < best_cnt:
                    best_cnt = cnt
                    best_mask = mask
                    best_i = i
                    if cnt == 1:
                        break

            # Work on the chosen cell
            r, c = empties.pop(best_i)
            b = box_id(r, c)
            mask = best_mask

            # Try each candidate digit by lowest set bit iteration
            while mask:
                bit = mask & -mask
                mask -= bit
                d = bit.bit_length()  # 1..9
                ch = chr(ord('0') + d)

                # place
                board[r][c] = ch
                rows[r] |= bit
                cols[c] |= bit
                boxes[b] |= bit

                if dfs():
                    return True

                # undo
                board[r][c] = '.'
                rows[r] ^= bit
                cols[c] ^= bit
                boxes[b] ^= bit

            # restore this position for other branches
            empties.insert(best_i, (r, c))
            return False

        dfs()
