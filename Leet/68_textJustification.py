# Approach:
# 1. Greedy pack words into a line until adding the next word would exceed maxWidth.
# 2. For each full line (not last):
#    - If one word: left-justify (word + spaces).
#    - Else: distribute spaces evenly; left slots get +1 when spaces don't divide evenly.
# 3. Last line: left-justify with single spaces, then pad right to maxWidth.
# Time: O(total characters), Space: O(maxWidth) per line.

class Solution:
    def fullJustify(self, words, maxWidth):
        res = []
        line_words = []
        line_len = 0  # total chars of words (no spaces)

        i = 0
        n = len(words)

        while i < n:
            w = words[i]
            # Check if we can add this word to current line
            # Needed width = current words + spaces between them (len(line_words)) + len(w)
            if line_words and line_len + len(line_words) + len(w) > maxWidth:
                # justify current line (not last line)
                res.append(self._justify_line(line_words, line_len, maxWidth))
                line_words = []
                line_len = 0
            else:
                line_words.append(w)
                line_len += len(w)
                i += 1

        # Last line: left-justify with single spaces
        last = " ".join(line_words)
        last += " " * (maxWidth - len(last))
        res.append(last)
        return res

    def _justify_line(self, line_words, line_len, maxWidth):
        # If only one word, left-justify
        if len(line_words) == 1:
            return line_words[0] + " " * (maxWidth - len(line_words[0]))

        total_spaces = maxWidth - line_len
        slots = len(line_words) - 1
        even_space = total_spaces // slots
        extra = total_spaces % slots  # leftmost 'extra' slots get +1 space

        parts = []
        for idx, w in enumerate(line_words):
            parts.append(w)
            if idx < slots:
                spaces_here = even_space + (1 if idx < extra else 0)
                parts.append(" " * spaces_here)
        return "".join(parts)
