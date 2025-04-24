# Program to swap three numbers without using format output

# Input three numbers
a = int(input("Enter first number (a): "))
b = int(input("Enter second number (b): "))
c = int(input("Enter third number (c): "))

print("\nBefore swapping:")
print("a =", a, ", b =", b, ", c =", c)

# Swap the values
temp = a
a = b
b = c
c = temp

print("\nAfter swapping:")
print("a =", a, ", b =", b, ", c =", c)
