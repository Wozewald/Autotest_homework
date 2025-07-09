# Пятое

first_list = [-10, 15, 30, -70, -150]

def filter_positive(numbers):
    positive_numbers = [num for num in numbers if num > 0]
    return positive_numbers

result = filter_positive(first_list)
print(result)

# Шестое

student = {"Имя": "Мария", "Возраст": 21}

inc = 3

def update_dict(student, inc):
    student["Возраст"] += inc
    return student

students = update_dict(student, inc)
print(students.get("Возраст"))
