''' operators
types of operators:
1. Arithmetic operators
2. Comparison operators
3. equality operators≈
4. Logical operators
5. Bitwise operators
6. shift operators
7. Assigment operators 
8. ternary operators
9. Membership operators
10.Identity operators

'''

# arithmetic operators
print("Arithmetic operators")
a = 10
b = 3
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b) #this operator returns a float value
print("Floor Division:", a // b) # this operator returns the largest integer less than or equal to the division result
print("Modulus:", a % b) # this operator returns the remainder of the division
print("Exponentiation:", a ** b) # this operator returns the result of raising a to the power of b
print("-------")

# comparison operators
print("Comparison operators")
x = 5
y = 10
print("Equal to:", x == y)
print("Not equal to:", x != y)
print("Greater than:", x > y)
print("Less than:", x < y)
print("Greater than or equal to:", x >= y)
print("Less than or equal to:", x <= y)
print("-------")

# equality operators
print("Equality operators")
a = 5
b = 5
print("Equal to:", a == b)
print("Not equal to:", a != b)
print("-------")

# logical operators
print("Logical operators")
p = True
q = False
print("Logical AND:", p and q)
print("Logical OR:", p or q)
print("Logical NOT:", not p)
print("-------")

# bitwise operators
# these operators work on the binary representation of integers
print("Bitwise operators")
m = 5  # binary: 0101
n = 3  # binary: 0011
print("Bitwise AND:", m & n)  # binary: 0001, decimal: 1
print("Bitwise OR:", m | n)   # binary: 0111, decimal: 7
print("Bitwise XOR:", m ^ n)  # binary: 0110, decimal: 6
print("Bitwise NOT:", ~m)   # binary: 1010, decimal: -6 (two's complement representation)
print("Bitwise Left Shift:", m << 1)  # binary: 1010
print("Bitwise Right Shift:", m >> 1)  # binary: 0010
# these are used to manipulate individual bits of integers, which can be useful in low-level programming, cryptography, and performance optimization. 
# is not commonly used in everyday programming, but it is important to understand how they work and when to use them.

# shift operators
# these operators shift the bits of a number to the left or right, effectively multiplying or dividing the number by powers of two.
print("Shift operators")
a = 5  # binary: 0101
print("Left Shift:", a << 1)  # binary: 1010, decimal: 10
print("Right Shift:", a >> 1)  # binary: 0010, decimal: 2
print("-------")

# assignment operators
print("Assignment operators")
x = 5
x += 3  # equivalent to x = x + 3
print("Addition Assignment:", x)
x -= 2  # equivalent to x = x - 2
print("Subtraction Assignment:", x)
x *= 4  # equivalent to x = x * 4
print("Multiplication Assignment:", x)
x /= 2  # equivalent to x = x / 2
print("Division Assignment:", x)
x %= 3  # equivalent to x = x % 3
print("Modulus Assignment:", x) 
print("-------")

# ternary operators
print("Ternary operators")
age = 20
status = "Adult" if age >= 18 else "Minor"
print("Status:", status)
# explanation: The ternary operator is a shorthand way of writing an if-else statement. 
# It evaluates the condition (age >= 18) and returns "Adult" if the condition is true, 
# or "Minor" if the condition is false.
# the logic is: condition ? value_if_true : value_if_false

# membership operators
print("Membership operators")
fruits = ["apple", "banana", "cherry"]
print("Is 'banana' in fruits?", "banana" in fruits)
print("Is 'grape' not in fruits?", "grape" not in fruits)
# explanation: The membership operators are used to test whether a value is present in a sequence (like a list, tuple, or string). 
# The 'in' operator returns True if the value is found in the sequence, while the 'not in' operator returns True if the value is


