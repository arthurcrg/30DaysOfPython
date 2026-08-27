it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}

print(len(it_companies))

it_companies.add('Twitter')
print(it_companies)

it_companies.update(['LinkedIn', 'Snapchat'])
print(it_companies)

it_companies.remove('IBM')
print(it_companies)

#remove returns an error if the element is not found, discard does not return an error
it_companies.discard('Oracle')
print(it_companies)