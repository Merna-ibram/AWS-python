def calculation(a, b):
    sum_result = a + b
    sub_result = a - b
    return sum_result, sub_result


num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

sum_result, result_sub = calculation(num1, num2)

print(f"Addition result: {sum_result}")
print(f"Subtraction result: {result_sub}")