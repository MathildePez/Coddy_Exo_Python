# initialiser le dictionnaire
student_records = {}

# fonction ajout étudiants
def add_student(name,age,courses):
    if name in student_records:
        print(f"Student '{name}' already exists.")
    else:
        student_records[name] = {
            "age": age, 
            "grades": set(), 
            "courses": set(courses)
            }
        print(f"Student '{name}' added successfully.")

 # fonction ajout note
def add_grade(name,grade):
    if name in student_records:
        student_records[name]["grades"].add(grade)
        print(f"Grade {grade} added for student '{name}'.")
    else:
        print(f"Student '{name}' not found.")

# fonction est inscrit
def is_enrolled(name,course):
    if name in student_records:
        return course in student_records[name]["courses"]
    else:
        print(f"Student '{name}' not found.")
        return False

# fonction moyenne de notes
def calculate_average_grade(name):
    if name in student_records:
        grades = student_records[name]["grades"]
        if not grades:
            return 0
        return sum(grades) / len(grades)
    else:
        print(f"Student '{name}' not found.")
        return None

# fonction liste étudiants par cours
def list_students_by_course(course):
    list_students = []
    for students,courses in student_records.items():
        if course in courses["courses"]:
            list_students.append(students)
    return list_students

# fonction meilleur étudiant
def filter_top_students(treshold):
    list_best_students = []
    for students in student_records:
        if calculate_average_grade(students) > treshold:
            list_best_students.append(students)
    return list_best_students

add_student("Alice", 20, ["Math", "Physics"])
add_student("Bob", 22, ["Math", "Biology"])
add_student("Diana", 23, ["Chemistry", "Physics"])
add_grade("Alice", 90)
add_grade("Alice", 85)
add_grade("Bob", 75)
add_grade("Diana", 95)

print(filter_top_students(80))  # Should return ["Alice", "Diana"]
print(filter_top_students(90))  # Should return ["Diana"]
print(filter_top_students(100))  # Should return an empty list
