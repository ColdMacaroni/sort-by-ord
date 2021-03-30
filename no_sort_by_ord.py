##
# no_sort_by_ord.py
# Sorts input string by the value given by ord(char)
# Dago
# 2021-03-31


def str_to_ord(string):
    """
    Returns a list with the ord of each character.
    """
    return [ord(x) for x in string]


def corresp_ord(string):
    """
    Returns a dictionary of the equivalent ascii order for each
    character. Including spaces. {82: 'S'}
    """
    dict_ord = {}
    for char in string:
        dict_ord[ord(char)] = char

    return dict_ord


def manual_sort(int_iterable):
    """
    Takes an iterable(only accepts integers) and sorts it manually.
    Not using the built-in sort function.
    """
    sorted_list = []

    # Will run until the original list is empty
    while len(int_iterable):
        # Get a starting value
        smallest = int_iterable[0]

        # Replace smallest with the actual smallest item
        for item in int_iterable:
            if smallest > item:
                smallest = item

        sorted_list.append(int_iterable.pop(int_iterable.index(smallest)))

    return sorted_list


def sort_by_ord(string):
    """
    Sorts a string by the value given by ord(char
    """
    # Set up
    list_ord = str_to_ord(string)
    dict_ord = corresp_ord(string)

    sorted_ord = manual_sort(list_ord)

    new_string = []

    # Convert each number to their corresponding character
    for item in sorted_ord:
        new_string.append(dict_ord[item])

    return ''.join(new_string)


def sort_each_word_by_ord(string):
    """
    Returns each word of a sentence sorted by result of ord(char)
    """
    # Setup
    sentence = string.split()
    new_sentence = []

    # Go through each word
    for word in sentence:
        new_sentence.append(sort_by_ord(word))

    return ' '.join(new_sentence)

if __name__ == "__main__":
    print(sort_by_ord(input('Sort all: ')))
    print(sort_each_word_by_ord(input('Sort by word: ')))
