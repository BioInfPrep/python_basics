import os
from itertools import groupby


def get_list_of_files(path="."):
    # see previous excercise
    pass


def get_extension(file):
    ext = os.path.splitext(file)[-1]
    # What happens if the extension is empty?
    pass


def get_file_types(list_files):
    pass


def main():
    file_list = get_list_of_files()
    sorted_files = get_file_types(file_list)


# execute the main function only
if __name__ == "__main__":
    main()
