# Author        : Ciaran O hOgain
# Version       : v1.0.0
# Description   : Print module and grade details of student.


student_numbers = ("L12345", "L54321")
module_subjects = ("Neural Networks", "Data Structures")
neural_net_grades = {student_numbers[0]: 40, student_numbers[1]: 70}
data_struct_grades = {student_numbers[0]: 55, student_numbers[1]: 82}

student_info_query = input("Please enter a student number\n")

if student_info_query == student_numbers[0]:
    print("Modules: {}".format(module_subjects))
    print("Grades: {} = {}%, {} = {}% ".format( module_subjects[0], neural_net_grades[student_numbers[0]], module_subjects[1], data_struct_grades[student_numbers[0]]))
else:
    print("Modules: {}".format(module_subjects))
    print("Grades: {} = {}%, {} = {}% ".format(module_subjects[0], neural_net_grades[student_numbers[1]], module_subjects[1], data_struct_grades[student_numbers[1]]))

