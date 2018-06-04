def divide(a, b):
    try:
        return a/b
    except ZeroDivisionError:
        print("there is a divide by zero error")
        return 0

x = float(input('enter a number'))
y = float(input("enter value by which you want to divide"))
result = divide(x, y)
print(result)