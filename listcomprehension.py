num = int(input("enter a number:"))
even = [i for i in range (1,num+1)if num % 2 == 0]
odd = [i for i in range (1,num+1)if num % 2 != 0]
print("even numbers:", even)
print("odd numbers:", odd)