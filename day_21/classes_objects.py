# Creating a class
class Person:
    pass
print(Person)  # <class '__main__.Person'> 

# Creating an object
p = Person()
print(p)  # <__main__.Person object at 0x7f8b1c2d1d30>

# Class constructor: it is a special method that is called when an object is created. It is used to initialize the object's attributes.
class Person:
      def __init__ (self, name): # self is a reference to the current instance of the class. It is used to access variables that belong to the class.
          self.name =name

p = Person('Link')
print(p.name)
print(p)

# Adding more attributes to the class
class Person:
      def __init__(self, firstname, lastname, age, country, city):
          self.firstname = firstname
          self.age = age
          self.country = country
          self.city = city


p = Person('Link', 117, 'Hyrule', 'Hyrule Castle Town')
print(p.firstname)
print(p.age)
print(p.country)
print(p.city)

# Object methods: they are functions that belong to the class and can be called on an object of the class. They are used to define the behavior of the object.
class Person:
      def __init__(self, firstname, lastname, age, country, city):
          self.firstname = firstname
          self.age = age
          self.country = country
          self.city = city
      def person_info(self):
        return f'{self.firstname} is {self.age} years old. He lives in {self.city}, {self.country}'

p = Person('Link', 117, 'Hyrule', 'Hyrule Castle Town')
print(p.person_info())

# Object default methods: they are special methods that are called when an object is created. They are used to define the behavior of the object when it is printed or converted to a string.
class Person:
    def __init__(self, firstname, lastname, age, country, city):
              self.firstname = firstname
              self.age = age
              self.country = country
              self.city = city
    def person_info(self):
            return f'{self.firstname} is {self.age} years old. He lives in {self.city}, {self.country}'

p1 = Person()
print(p1.person_info())
p2 = Person('John', 'Doe', 30, 'Nomanland', 'Noman city')
print(p2.person_info())

# Method to Modify Class Default Values
class Person:
    def __init__(self, firstname, lastname, age, country, city):
              self.firstname = firstname
              self.age = age
              self.country = country
              self.city = city
    def person_info(self):
            return f'{self.firstname} is {self.age} years old. He lives in {self.city}, {self.country}'
    def add_skill(self, skill):
          self.skills.append(skill)

p1 = Person()
print(p1.person_info())
p1.add_skill('Swordsmanship')
p1.add_skill('Archery')
p1.add_skill('Stealth')
p2 = Person('John', 'Doe', 30, 'Nomanland', 'Noman city')
print(p2.person_info())
print(p1.skills)
print(p2.skills)

# Inheritance: it is a way to create a new class from an existing class. The new class is called the child class and the existing class is called the parent class. The child class inherits the attributes and methods of the parent class.
class Student(Person):
    pass



s1 = Student('John', 'Doe', 30, 'Finland', 'Helsinki')
s2 = Student('Joana', 'Doe', 28, 'Finland', 'Espoo')
print(s1.person_info())
s1.add_skill('JavaScript')
s1.add_skill('React')
s1.add_skill('Python')
print(s1.skills)

print(s2.person_info())
s2.add_skill('Organizing')
s2.add_skill('Marketing')
s2.add_skill('Digital Marketing')
print(s2.skills)

# Overriding parent methods: it is a way to change the behavior of a method in the child class. The child class can have a method with the same name as the parent class, but with a different implementation.
class Student(Person):
    def __init__ (self, firstname='Asabeneh', lastname='Yetayeh',age=250, country='Finland', city='Helsinki', gender='male'):
        self.gender = gender
        super().__init__(firstname, lastname,age, country, city)
    def person_info(self):
        gender = 'He' if self.gender =='male' else 'She'
        return f'{self.firstname} {self.lastname} is {self.age} years old. {gender} lives in {self.city}, {self.country}.'

s1 = Student('John', 'Doe', 30, 'Finland', 'Helsinki','male')
s2 = Student('Joana', 'Doe', 28, 'Finland', 'Espoo', 'female')
print(s1.person_info())
s1.add_skill('JavaScript')
s1.add_skill('React')
s1.add_skill('Python')
print(s1.skills)

print(s2.person_info())
s2.add_skill('Organizing')
s2.add_skill('Marketing')
s2.add_skill('Digital Marketing')
print(s2.skills)

