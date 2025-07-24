n = float(input("Enter a number to convert to binary: "))
integer_part = int(n)
fractional_part = n - integer_part

# Convert integer part
binary_integer = ""
if integer_part == 0:
    binary_integer = "0"
else:
    while integer_part > 0:
        binary_integer = str(integer_part % 2) + binary_integer
        integer_part = integer_part // 2

# Convert fractional part (limit to 8 digits)
binary_fraction = ""
count = 0
while fractional_part > 0 and count < 8:
    fractional_part *= 2
    bit = int(fractional_part)
    binary_fraction += str(bit)
    fractional_part -= bit
    count += 1

# Combine
print("Binary:", binary_integer + "." + binary_fraction)
