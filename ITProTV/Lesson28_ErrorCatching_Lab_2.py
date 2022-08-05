# Program to read a file name passed as a command-line argument and print the number of lines, words, and characters in the file
# Import the built-in sys module
import sys

if __name__ == "__main__":
    numArgs = len(sys.argv)
if numArgs == 1:
    myArg = input("Enter the file name:")
else:
    myArg = sys.argv[1]
try:
    #file=open(myArg)
    raise FileError(file=open(myArg))
except IOError as e:
    print("The specified file does not exist.")
except Exception as e:
  print("This message is displayed because you have raised an exception FileError to prevent the error.")
# The with block follows. Open the file passed as a command-line argument in the read mode.
else:
    with open(myArg, "r") as fhand:
        num_lines = 0
        num_words = 0
        num_chars = 0
    # Read each line from the file using for loop
        for line in fhand:
            words = line.split()
            num_lines += 1
            num_words += len(words)
            num_chars += len(line)
# Print the number of lines, words, and characters in the file
    print("Number of lines in the file:", num_lines)
    print("Number of words in the file:", num_words)
    print("Number of characters in the file:", num_chars)
    file.close()
finally:
    print("The program is complete.")
