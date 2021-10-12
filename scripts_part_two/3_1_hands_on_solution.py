import os
from itertools import groupby
from collections import Counter


def get_list_of_files(path="."):
    only_files = [f for f in os.listdir(path) if os.path.isfile(f)]
    return only_files


def get_extension(file):
    ext = os.path.splitext(file)[-1]
    if ext == "":
        return "No extension found"
    return ext


def get_file_types(list_files):
    sorted_list_files = sorted(list_files, key=get_extension)
    files_by_type = groupby(sorted_list_files, key=get_extension)
    return files_by_type


def main():
    file_list = get_list_of_files()
    sorted_files = get_file_types(file_list)
    print("In the current working directory there are %s files" % len(file_list))
    # Option 1 with itertools
    print("OPTION 1")
    for key, group in sorted_files:
        print("%s: %i file(s)" % (key, len(list(group))))
    # Option 2 with Counter
    print("OPTION 2")
    modified_file_list = [get_extension(f) for f in file_list]
    counter_extensions = Counter(modified_file_list)
    for key, value in counter_extensions.items():
        print("%s: %i file(s)" % (key, value))
    # Printing into a file
    with open("my_dir_stats.txt", "w") as f:
        for key, group in get_file_types(file_list):
            f.write("%s: %i file(s)\n" % (key, len(list(group))))


# execute the main function only
if __name__ == "__main__":
    main()
