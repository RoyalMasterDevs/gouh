# Variable that stores a day of the week
day_of_week = "Friday"

# If statement
if day_of_week == "Friday":
    print(f"Hurray! It's {day_of_week}, the weekend is just around the corner.")
else:
    print(f"It's {day_of_week}, stay strong and motivated, the weekend is coming soon!")

# Variable that stores a number
number = 30
# Multiple if (elif) statement
if number < 0:
    print("You have chosen a negative number!")
elif 0 <= number < 10:
    print("You have chosen a small number!")
elif 10 <= number < 20:
    print("You have chosen a medium size number!")
else:
    print("Wow, that's a big number!")
