#Program to demonstrate the use of functions in os module
print("Importing the os module to access the built-in functions…")
import os#Display the location of the current directory
print("The path of the current working directory is:",os.getcwd())
#Rename “sample.txt” to “dummy.txt” in the CWD
os.rename("sample.txt", "dummy.txt")

print("The name of the file sample.txt has been changed to dummy.txt")
os.rename("dummy.txt", "sample.txt")
print("The name of the file dummy.txt has been changed to sample.txt")#Rename the folder “sampledir” to “dummydir” in the CWD
os.rename("sampledir", "dummydir")
print("The name of the folder sampledir has been changed to dummydir")