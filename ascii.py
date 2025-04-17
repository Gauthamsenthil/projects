# Program to check the ASCII code of different alphabets

# Get input from the user
text = input("Enter alphabets: ")

# Loop through each character and print its ASCII code
print("\nCharacter : ASCII Code")
for char in text:
    if char.isalpha():  # Check if the character is an alphabet
        print("char = " ,{ord(char)})
    else:
        print(char," is not an alphabet")
# Program to check the ASCII code of different alphabets


