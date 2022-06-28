Student_list = ['John', 'Smith', 'Kathy', 'Philip']
#call a list
print(Student_list)
#print the first item of the list
print(Student_list[0])
#print the second item of the list
print(Student_list[1])
#print the thirdd item of the list
print(Student_list[2])
#print the fourth item of the list
print(Student_list[3])
#To replace Smith with Steve in the list
Student_list[1] = 'Steve'
print("Student List: ", Student_list)
#To add a new student to the list
Student_list.append('Mark')
#To print the updated list with a new student added
print("The updated list with a new student added is: ", Student_list)
#To search for a student name in the list
IndexNumber1 = Student_list.index("Kathy")
print(IndexNumber1)
#To delete a student name in the list from a specific index
del Student_list[2]
print("The final list after deleting Kathy is: ", Student_list)