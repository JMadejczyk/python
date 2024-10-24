students = {}
tests = {}

n = int(input())

for line in range(0, n):
    elements = [x for x in input().split(" ")]
    student_name = elements[0]
    exam_grades = []
    for exam in elements[1:]:
        exam_name, grade = exam.split(":")
        exam_grades.append(float(grade))
    students[student_name] = sum(exam_grades)/len(exam_grades)
    if exam_name not in tests:
        tests[exam_name] = [float(grade)]
    else:
        tests[exam_name].append(float(grade))

students_sorted = sorted(students)
tests_sorted = sorted(tests)

for test in tests_sorted:
    summ = sum(tests[test])
    lenn = len(tests[test])
    print(f"{test} {summ/lenn}")
    


    
    