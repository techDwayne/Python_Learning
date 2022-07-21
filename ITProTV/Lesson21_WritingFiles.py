
output_filename = 'output.txt'
#with open (output_filename, 'a')as file:
 #   file.write('Yayyyy!!\n')
with open('data.txt', 'r') as in_file, open(output_filename,'w') as output:
    for line in in_file:
        if line!='\n':
            output.write(line)