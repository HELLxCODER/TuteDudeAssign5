student_list ={'Alice': 90, 'Barry': 71, 'Conner': 81, 'Darvin': 99}
name_student = input("Enter students name: ")
if name_student in student_list:
    print(f"{name_student}'s marks are: {student_list[name_student]}")
else:
    print(f"{name_student}, is not found.")