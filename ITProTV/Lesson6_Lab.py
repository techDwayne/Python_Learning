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
print('Index for Kathy in the whole list is: ', IndexNumber1)
#To delete a student name in the list from a specific index
del Student_list[2]
print("The final student list after deleting Kathy is: ", Student_list)
#To sort the list in ascending order
Student_list.sort()
#To print the sorted list in ascending order
print('The sorted list in ascending order is: ', Student_list)
#To sort the list in descending order
Student_list.sort(reverse=True)
#To print the sortedlist in descending order
print('The sorted list in descending order is: ', Student_list)
#To reverse list the items
Student_list.reverse()
#To print the reversed list
print('The reverse list is: ', Student_list)



