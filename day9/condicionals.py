# If Condition
a = 3
if a > 0: #if a is greater than 0, this will happen:
    print('A is a positive number') # A is a positive number

# If Else Condition
a = 3
if a < 0: #if a is greater than 0, this will happen:
    print('A is a negative number')
else: #if it isn't, this will happen:
    print('A is a positive number')

# If Elif Else Condition
a = 0
if a > 0: #if a is greater than 0, this will happen:
    print('A is a positive number')
elif a < 0: #if a is less than 0, this will happen:
    print('A is a negative number')
else: #the only other option is that a is equal to 0, so this will happen:
    print('A is zero')

# Short Hand If
a = 3
print('A is positive') if a > 0 else print('A is negative') # same thing, but in one line

# Nested If
a = 0
if a > 0: #if a is greater than 0, this will happen:
    if a % 2 == 0: #if a is greater than 0 and, when divided by 2, the remainder is 0, this will happen:
        print('A is a positive and even integer')
    else: # if a is greater than 0 and, when divided by 2, the remainder is not 0, this will happen:
        print('A is a positive and odd number')
elif a == 0: #if a is equal to 0, this will happen:
    print('A is zero')
else: # the only other option is that a is less than 0, so this will happen:
    print('A is a negative number')

# If and Logic Operators

# and
a = 0
if a > 0 and a % 2 == 0: # if a is greater than 0 and, when divided by 2, the remainder is 0, this will happen:
        print('A is an even and positive integer')
elif a > 0 and a % 2 !=  0: # if a is greater than 0 and, when divided by 2, the remainder is not 0, this will happen:
        print('A is an odd and positive integer')
elif a == 0: #if a is equal to 0, this will happen:
    print('A is zero')
else: # the only other option is that a is less than 0, so this will happen:
    print('A is negative')

# or
user = 'John Pork'
access_level = 3
if user == 'admin' or access_level >= 4:
        print('Access granted!')
else:
    print('Access denied!')