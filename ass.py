
student_dict = {'student name': 'marks'}
student_name = input('Enter student name: ')
student_marks = float(input('Enter marks: '))
student_dict.update({student_name: student_marks})
print(student_dict)
search_name = input('Enter student name: ')
print(student_dict.get(search_name, 'Student not found'))