class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        count = 0
        
        for num in range(low, high + 1):
            s = str(num)
            if len(s) % 2 != 0:
                continue  # skip odd-length numbers
            
            n = len(s) // 2
            first_half = sum(int(d) for d in s[:n])
            second_half = sum(int(d) for d in s[n:])
            
            if first_half == second_half:
                count += 1
        
        return count
