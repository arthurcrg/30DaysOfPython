print('{} {} of {}'.format(30, 'days', 'Python'))
print('{} for {}'.format('Coding', 'everyone'))

company = 'Coding for All'
print(len(company))  # length of the string
print(company.upper())  # converts all characters to uppercase  
print(company.lower())  # converts all characters to lowercase
print(company.title())  # converts the first character of each word to uppercase
print(company[7:-1])  # slices out the first six characters of the string
print(company.startswith('Coding'))  # checks if the string starts with 'Coding'
print(company.replace('All', 'Everyone'))  # replaces 'All' with 'Everyone'
print(company[0], company[7].capitalize(), company[11])