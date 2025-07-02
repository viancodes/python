# String Methods in Python - Complete Demonstration with Examples

# Original string for demonstration
text = "  Hello World! Welcome to Python 123.  "

# ------------------------------
# CASE CONVERSION METHODS
# ------------------------------
print("# CASE CONVERSION METHODS")
print("Original:", text)
print("lower():", text.lower())        # Expected: "  hello world! welcome to python 123.  "
print("upper():", text.upper())        # Expected: "  HELLO WORLD! WELCOME TO PYTHON 123.  "
print("capitalize():", text.capitalize())  # Expected: "  hello world! welcome to python 123.  "
print("title():", text.title())        # Expected: "  Hello World! Welcome To Python 123.  "
print("swapcase():", text.swapcase())  # Expected: "  hELLO wORLD! wELCOME TO pYTHON 123.  "
print()

# ------------------------------
# WHITESPACE AND CHARACTER REMOVAL
# ------------------------------
print("# WHITESPACE AND CHARACTER REMOVAL")
print("strip():", text.strip())        # Removes leading and trailing whitespace
print("lstrip():", text.lstrip())      # Removes leading whitespace
print("rstrip():", text.rstrip())      # Removes trailing whitespace
print("replace('o', '0'):", text.replace('o', '0'))  # Replace all 'o' with '0'
print()

# ------------------------------
# SEARCHING AND FINDING
# ------------------------------
print("# SEARCHING AND FINDING")
print("find('Python'):", text.find('Python'))    # Returns index of 'Python'
print("find('Java'):", text.find('Java'))        # Returns -1 (not found)
print("index('World'):", text.index('World'))    # Returns index of 'World'
# print("index('Java'):", text.index('Java'))    # Would raise ValueError
print("startswith('  Hello'):", text.startswith('  Hello'))  # True
print("endswith('123.  '):", text.endswith('123.  '))        # True
print("count('o'):", text.count('o'))             # Count how many 'o' characters
print()

# ------------------------------
# SPLITTING AND JOINING
# ------------------------------
print("# SPLITTING AND JOINING")
words = text.strip().split()                     # Splits on whitespace
print("split():", words)                         # Expected list of words
joined = '-'.join(words)
print("join():", joined)                         # Joins with hyphen
print()

# ------------------------------
# CHARACTER TYPE CHECKS
# ------------------------------
print("# CHARACTER TYPE CHECKS")
sample1 = "Python"
sample2 = "12345"
sample3 = "Python123"
sample4 = "    "
sample5 = "lowercase"
sample6 = "UPPERCASE"

print("isalpha('Python'):", sample1.isalpha())   # True
print("isdigit('12345'):", sample2.isdigit())    # True
print("isalnum('Python123'):", sample3.isalnum()) # True
print("isspace('    '):", sample4.isspace())     # True
print("islower('lowercase'):", sample5.islower()) # True
print("isupper('UPPERCASE'):", sample6.isupper()) # True
print()

# ------------------------------
# FORMATTING AND ALIGNMENT
# ------------------------------
print("# FORMATTING AND ALIGNMENT")
text2 = "Python"
print("center(20, '*'):", text2.center(20, '*'))  # Center with '*'
print("ljust(20, '-'):", text2.ljust(20, '-'))    # Left align with '-'
print("rjust(20, '#'):", text2.rjust(20, '#'))    # Right align with '#'
