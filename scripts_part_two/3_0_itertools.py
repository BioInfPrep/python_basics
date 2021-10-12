# Getting to know itertools
#
# Import groupby
from itertools import groupby
from collections import Counter


def keyfunc(el):
    """From the given string, if the first letter is CAP, then return upper, otherwise Lower

    Args:
        el (string)

    Returns:
        string: either Upper or Lower
    """
    if el[0].isupper():
        return 'Upper'
    return 'Lower'


my_list = ['B', 'i', 'o', 'I', 'n', 'f',
           'o', 'r', 'm', 'a', 't', 'i', 'c', 's']
print(sorted(my_list))
my_list = sorted(my_list, key=keyfunc)
print(my_list)  # Do you notice any difference?

grouped_list = groupby(my_list, keyfunc)
for key, group in grouped_list:
    print('starts with', key, '->', ' '.join(list(group)))

# What does groupby return?
# What happens when you remove sorting?

# Another package is collections, see above for import
modified_list = [keyfunc(el) for el in my_list]
counter_words = Counter(modified_list)
print('counter words:', counter_words)
# to access the grouped elements you'll need to call the items
for key, val in counter_words.items():
    print('starts with', key, '->', val)
