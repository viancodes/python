# Approach:
# 1. Use two pointers starting from the end of both strings (least significant bits).
# 2. Add corresponding bits along with carry.
# 3. Append result bit (sum % 2) to output and update carry = sum // 2.
# 4. Continue until both strings and carry are processed.
# 5. Reverse the result and join as string.
# Time: O(max(len(a), len(b))), Space: O(max(len(a), len(b)))

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i, j = len(a) - 1, len(b) - 1
        carry = 0
        result = []
        
        while i >= 0 or j >= 0 or carry:
            total = carry
            if i >= 0:
                total += int(a[i])
                i -= 1
            if j >= 0:
                total += int(b[j])
                j -= 1
            
            result.append(str(total % 2))  # current bit
            carry = total // 2             # update carry
        
        return ''.join(reversed(result))
