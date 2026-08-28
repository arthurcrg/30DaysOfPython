# Grades

grade = int(input("Enter your grade: "))
if 0<=grade<=59:
    print("You got an F")
elif 60<=grade<=69:
    print("You got a D")
elif 70<=grade<=79:
    print("You got a C")
elif 80<=grade<=89:
    print("You got a B")
elif 90<=grade<=100:
    print("You got an A")
else:
    print("Invalid grade")

# Months

month = int(input("Enter a month number(1-12): "))
if month == 9 or month == 10 or month == 11:
    print("It's Autumn")
elif month == 12 or month == 1 or month == 2:
    print("It's Winter")
elif month == 3 or month == 4 or month == 5:
    print("It's Spring")
elif month == 6 or month == 7 or month == 8:
    print("It's Summer")
else:
    print("Invalid month number")

# Fruits
fruits = ['banana', 'orange', 'mango', 'lemon']
new_fruit = input("Enter a fruit name: ").lower()
if new_fruit in fruits:
    print("That fruit already exists in the list")
    print("The list of fruits is: ", fruits)
else:
    fruits.append(new_fruit)
    print("Fruit added to the list")
    print("This is the new list of fruits: ", fruits)
