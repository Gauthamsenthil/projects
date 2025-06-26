# Define a function to square a number
def square(n):
    return n * n

# Ask user for beginning and ending numbers
start = int(input("Enter the beginning number: "))
end = int(input("Enter the ending number: "))

# Create an empty list to store squares
squares = []

# Go from start to end
current = start
while current <= end:
    # Find square and add to list
    result = square(current)
    squares.append(result)
    current = current + 1

# Print the result
print("Squares from", start, "to", end, "are:", squares)
