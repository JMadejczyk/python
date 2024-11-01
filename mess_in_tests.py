N, S = [int(x) for x in input().split()]
names_with_indexes = [input() for _ in range(N)]
K = int(input())
tests_messy_info = [input() for _ in range(K)]

students = []
names_by_indexes = {}
for name_with_index in names_with_indexes:
    name, index = name_with_index.split()
    students.append({'name': name, "grades":[]})
    names_by_indexes[index] = name

def cal_grade(percent):
    if percent < 0.5:
        return 2
    elif percent < 0.7:
        return 3
    elif percent < 0.9:
        return 4
    else: return 5

def calculate_final_grade(grades):
    avg = sum(grades)/len(grades)
    if avg < 3:
        return 2
    elif avg < 3.5:
        return 3
    elif avg < 4.5:
        return 4
    else: return 5

for test in tests_messy_info:
    tab = test.split()
    if len(tab) == 2:
        first, second = tab
        points, max_points = [int(x) for x in second.split("/")]
        if first[:3] == "inf":
            index = first[3:]
            name = names_by_indexes[index]
        if first.isdecimal():
            index = first
            name = names_by_indexes[index]
        if first.isalpha():
            name = first
        
    elif len(tab) == 3:
        first, second, third = tab
        points, max_points = [int(x) for x in third.split("/")]
        if first.isalpha():
            name = first
        else:
            name = second
        points, max_points = [int(x) for x in third.split("/")]


    index = [student["name"] for student in students].index(name)
    students[index]["grades"].append(cal_grade(points/max_points))

print(students)
students.sort(key=lambda x: x["name"])

for student in students:
    while len(student["grades"]) < S:
            student["grades"].append(0)
    print(f"{student["name"]} {calculate_final_grade(student["grades"])}")

    