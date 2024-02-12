courses = ["MIT","Cybersecurity","Datascience"]

print(courses)
# Accessing an element in array
print(courses[1])

# Looping through array
for course in courses:
    print(course)

# Adding an ellement in an array
courses.append("Android Development")
print(courses)

# Deleting an ellement from an array
courses.remove("Datascience")
print(courses)