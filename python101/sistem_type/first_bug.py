# First Bug
print("*** First Bug ***")

# This code will generate a zero division error/exception
x = 10
y = 0

try:
    ratio = x / y
except ZeroDivisionError:
    print(f"Oops, you attempted to divide by zero {x} / {y}.")
