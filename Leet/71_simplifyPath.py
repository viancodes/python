# Approach:
# 1. Split path by "/" → gives parts (some empty, ".", "..", or valid dirs/files).
# 2. Use a stack to build the canonical path:
#    - If part == "" or ".", skip (means current dir or redundant slash).
#    - If part == "..", pop stack if not empty (go up one level).
#    - Else: push part to stack (valid directory/file name).
# 3. Join stack with "/" and prepend root "/".
# 4. If stack is empty → return "/".
# Time: O(n), Space: O(n).

class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        parts = path.split("/")

        for part in parts:
            if part == "" or part == ".":
                continue
            elif part == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(part)

        return "/" + "/".join(stack)
