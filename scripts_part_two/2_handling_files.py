# Handling files

# open file for writing
with open("new_file.txt", "w") as f:
    # only strings can be written to the file:
    for i in range(10):
        f.write(str(i)+"\n")


# open file for reading
with open("new_file.txt", "r") as f:
   # get text from file:
    a = f.read()
    print("A", a)
    # Only uncomment b and c, if a is commented
    # b = f.readline()
    # c = f.readlines()
    # print(b)
    # print(c)

    # If all three variables (a,b,c) are run
    # B and C are empty, since A already "took" the whole information
    # (Speaking in a really simplified way)
    # If A is commented, then B only contains "0",
    # since it reads only one line,
    # But C contains all other lines but "0", since it was already read by B
