import re
from collections import Counter


def load_data(filepath):
    with open(filepath, 'r') as data:
        return data.read()


def get_most_frequent_words(text):
    words = get_all_words(text)
    cntr = Counter(words)
    print(cntr.most_common(10))


def get_all_words(text):
    words = re.findall(r'[^\W|\d]+', text) #De Morgan's law
    return words


if __name__ == '__main__':
    filepath = input('Name of the file:')
    text_from_file = load_data(filepath)
    get_most_frequent_words (text_from_file)