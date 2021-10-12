# file handlingwith open('iris.csv', 'r') as file_handle: # open file for reading ‘r’    entire_file_text = file_handle.read()    print(entire_file_text[:300])  # print only part of the file cave: Number indicates CHARS!!!with open('iris.csv', 'r') as file_handle:  # open file for reading ‘r’    file_lines = file_handle.readlines()  # returns a list    print(' '.join(file_lines[:2]))  # print first 2 lines    column_names = file_lines[0].split(';')  # get column names    print(column_names)
# file handling
with open('iris.csv', 'r') as file_handle:  # open file for reading ‘r’
    entire_file_text = file_handle.read()
    # prints only part of the file cave
    print(entire_file_text[:250])
    # The first 250characters, not lines!

with open('iris.csv', 'r') as file_handle:  # open file for reading ‘r’
    file_lines = file_handle.readlines()  # returns a list
    print(' '.join(file_lines[:2]))  # print first 2 lines
    column_names = file_lines[0].split(';')  # get column names
    print(column_names)
