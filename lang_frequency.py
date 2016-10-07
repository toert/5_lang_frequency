import re
from collections import Counter


def load_data(filepath):
    with open(filepath, 'r') as data:
        return data.read()


def get_most_frequent_words(text, number_of_words_to_output):
    words = get_all_words(text)
    counter_words = Counter(words)
    list_of_common_words = \
        counter_words.most_common(number_of_words_to_output)
    return list_of_common_words


def get_all_words(text):
    words = re.findall(r'[^\W|\d]+', text)
    return words


if __name__ == '__main__':
    number_of_output_words = 10
    filepath = input('Name of the file:')
    text_from_file = load_data(filepath)
    text_from_file.lower()
    list_of_common_words = get_most_frequent_words(text_from_file, \
                                                   number_of_output_words)
    print('{} {}'.format(str(number_of_output_words), \
                         'of the most common words: '))
    for word in list_of_common_words:
        print(word)