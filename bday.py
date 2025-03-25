# Create an empty list to store birthdays
birthdays = []
##hello
# Loop to accept 5 birthday dates
for i in range(5):
    date = input(f"Enter birthday {i+1} (YYYY-MM-DD): ")
    birthdays.append(date)

# Print the stored birthdays
print("\nStored Birthdays:")
for i, date in enumerate(birthdays, start=1):
    print(f"Birthday {i}: {date}")
