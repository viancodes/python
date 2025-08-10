class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # Handle zero case
        if num1 == "0" or num2 == "0":
            return "0"
        
        m, n = len(num1), len(num2)
        result = [0] * (m + n)  # Max length of result = m + n
        
        # Reverse iterate to simulate multiplication
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                mul = (ord(num1[i]) - ord('0')) * (ord(num2[j]) - ord('0'))
                sum_ = mul + result[i + j + 1]  # Add carry from previous step
                
                result[i + j + 1] = sum_ % 10
                result[i + j] += sum_ // 10
        
        # Skip leading zeros
        res_str = ''.join(map(str, result)).lstrip('0')
        return res_str if res_str else "0"
