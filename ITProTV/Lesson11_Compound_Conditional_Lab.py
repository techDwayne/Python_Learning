#Program to check the eligibility of a student based on the credit score and GPA
#Accept credit score and GPA
studentcredit = int(input("Enter the student’s credit score:"))
GPA = int(input("Enter the student’s GPA:"))
#Compound conditional statement to check the input against the criteria
if studentcredit>=140 and GPA>=3.0:
 print("Congratulations! You are eligible for a Graduation Program at Loyola University, Chicago.")
elif studentcredit<140 and studentcredit>=120 and GPA>=3.0:
 print("Congratulations! You are eligible for a Graduation Program at University of South Carolina.")
elif studentcredit<120 and studentcredit>100 and GPA>=2.0:
 print("Congratulations! You are eligible for a Graduation Program at University of Notre Dame.")
else:
 print("Your credit score or GPA is low. Try again next year.")
 