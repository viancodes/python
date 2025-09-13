class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        # Iterate over the string and remove the first digit
        # such that the next digit is greater (greedy choice)
        for i in range(len(number) - 1):
            if number[i] == digit and number[i] < number[i + 1]:
                return number[:i] + number[i+1:]
        
        # If no such case found, remove the last occurrence
        idx = number.rfind(digit)
        return number[:idx] + number[idx+1:]
