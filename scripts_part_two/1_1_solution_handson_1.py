# solution: listdir file printing
import os
all_files = os.listdir()
for file in all_files:
    print(file)

print("The total number of files is " + str(len(all_files)))
# or a more elegant way to print:
print("The total number of files is %i" % (len(all_files)))
# this method is called string formatting
# it simplifies the inclusion of variables in strings
# for example, you don't need to modify the type of the variable to append it to the string

# Solution Additional task:

only_files = []  # create list for only files
for f in all_files:  # iterate all_files
    if os.path.isfile(f):  # check if f is a file
        only_files.append(f)  # add to list
        print(f)

print("In the current working directory there are %s files" % len(only_files))
# More advanced ways:

# The following line is a more advanced way of producing/modifying lists
# It is called list comprehension
# It has the form [output_el for iteration_el in existing_list]
# At the end, yu can also add an if condition as in the example below

only_files = [f for f in all_files if os.path.isfile(f)]
print("In the current working directory there are %s files" % len(only_files))

# Filtering lists:
# Another way of filtering the list is by using the filter option.
# since os.path.isfile is a function that returns a boolean value (True/False)
# it can be used to filter the all_files list
# Careful! filter returns a filter object, hence it needs to be converted to a list again
only_files = list(filter(os.path.isfile, all_files))
print("In the current working directory there are %s files" % len(only_files))
