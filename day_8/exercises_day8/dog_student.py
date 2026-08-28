dog = {}
dog["name"] = "John Pork"
dog["breed"] = "Pug"
dog["legs"] = 4
dog["age"] = 8
print(dog)

student = {}
student["first_name"] = "John"
student["last_name"] = "Doe"
student["gender"] = "Male"
student["age"] = 25
student["marital_status"] = "Single"
student["skills"] = ["Python", "JavaScript", "SQL"]
student["country"] = "Egypt"
student["city"] = "Cairo"
student["address"] = "123 Main St"
print(student)

print(len(student))
print(student["skills"])
print(type(student["skills"]))

student["skills"].append("HTML")
print(student["skills"])

print(list(student.keys()))
print(list(student.values()))

print(student.items())

student.pop("marital_status")
print(student)

del student
del dog