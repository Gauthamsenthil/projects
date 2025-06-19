n = input("enter the age :")
try:
    if type(n) == str:
        raise ValueError
    elif type(n) == float:
        raise ValueError
    elif type(n) == int:
        if n % 2 == 0:
            print("even")
        else:
            print("odd")
except ValueError:
    print("input error:you might have entered a float or string.please enter the integer value")

