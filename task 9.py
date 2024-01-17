def func(num1, num2):
    b = num1 % num2
    return b

try:
    n1 = int(input("enter friest num "))
    n2 = int(input("enter secound num "))
    print(func(n1, n2))
except ValueError:
    print("cannot be empty ")
except ZeroDivisionError:
    print("cannot by 0")

