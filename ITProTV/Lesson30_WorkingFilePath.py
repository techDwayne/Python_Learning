import os
current_directory = os.getcwd
directory_files = os.listdir()
filepath = os.path.join(current_directory(), 'message.txt')
messagetxt_stats = os.stat(filepath)
print("My Working directory: ", current_directory())
print(filepath)
#print("My Files: ",directory_files)
#print("Created: ", messagetxt_stats)