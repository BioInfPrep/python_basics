# Chap 0 - Flow Control
print("################################")
string_as_list = [x for x in "Python"]
for letter in string_as_list:
    if letter == "h":
        break
    print("Current letter: " + letter)

print("################################")

for letter in string_as_list:
    if letter == "h":
        continue
    print("Current letter: " + letter)
print("################################")

for letter in string_as_list:
    if letter == "h":
        pass
    print("Current letter: " + letter)
