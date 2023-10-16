def addition(a,b):
    result = a + b
    return result

right_arrow = "\u2192"
a = int(input("\nEnter first number: "))
b = int(input("\nEnter second number: "))

sum_result = addition(a,b)
print("\naddition",str((a,b)),right_arrow,sum_result) + "\n"