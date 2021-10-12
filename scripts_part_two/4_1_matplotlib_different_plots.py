import random
import matplotlib
import numpy as np
import matplotlib.pyplot as plt

plt.style.use('ggplot')

# example of a linechart
x = np.linspace(0, 3*np.pi, 500)
# what are the different parameters for linspace?
# print(x)  # what is happening here?
y = np.sin(x)
# print(y) # and here?
plt.plot(x, y)
plt.title('A simple chirp')
plt.xlabel('X label')
plt.ylabel('Y label')

# plt.show()  # Uncomment to show lineplot
plt.clf()  # This clears the previous input
################################

# Barchart

# example of a barchart
D1 = {'Label0': 26, 'Label1': 17, 'Label2': 30}
D2 = {'Label0': 16, 'Label1': 10, 'Label2': 10}
labels_x = np.arange(len(D1))
# What does arange do?
# print(labels_x)
# What do you expect to get here?
# print(np.arange(10))
plt.bar(labels_x, D1.values(), align='center', color='blue', width=0.4)
plt.bar(labels_x + 0.4, D2.values(), align='center', color='red', width=0.4)
plt.xticks(labels_x + 0.2, D1.keys())
# plt.show() # uncomment to see barplot
plt.clf()
#####################################

# Boxplot

# make a random subset
local_list = []
for i in range(3):
    local_list.append(random.sample(range(300*i, 1000 + 300*i), 100))
plt.boxplot(local_list, labels=['A', 'B', 'C'])
plt.savefig('exemplary_boxplot.png')  # write figure into a file #
# plt.show()
plt.clf()

################################

# Histogram

sepal_length = []
# open file for reading ‘r’
with open('iris.csv', 'r') as file_handle:
    file_lines = file_handle.readlines()
    print("headers", file_lines[0])
    for line in file_lines[1:]:  # iterate through lines in the file, ommit headers
        split_line = line.split(',')  # split by colon
        sepal_length_loop = float(split_line[0])
        sepal_length.append(sepal_length_loop)
plt.hist(sepal_length, bins=30)
plt.title("Histogram on sepal length")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Count")
# plt.show()
plt.clf()
