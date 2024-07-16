# Variable rules in Python
print("*** Variable rules in Python ***")

# 1. A variable name must start with a letter or underscore
_str = "This is a string"
print(_str)
num9 = 9
print(num9)  # 123Num is invalid and will cause a SyntaxError

# 2. A variable name cannot start with a number

# 3. A variable name can only contain alphanumeric characters and underscores (A-z, 0-9, and _)
num_num = 10
print(num_num)  # num-num is invalid, - (dash) is not allowed

# 4. Variable names are case-sensitive (age, Age and AGE are three different variables)
lpstr = "lowercase"
print(lpstr)
Str = "Uppercase"
print(Str)
STR = "UPPERCASE"
print(STR)

# Naming Conventions
print("*** Naming conventions in Python ***")

# 1. Variables and functions: Snake Case
user_name = "John Doe"  # Variable
print(user_name)

# 3. Constants: Uppercase Snake Case
PI_CONSTANT = 3.14159
print(PI_CONSTANT)
