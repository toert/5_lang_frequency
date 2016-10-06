import re
from collections import Counter


def load_data(filepath):
    with open(filepath, 'r') as data:
        return data.read()


def get_most_frequent_words(text,number_of_words_to_output):
    
    words = get_all_words(text)
    cntr = Counter(words)
    list_of_common_words = cntr.most_common(number_of_words_to_output)
    return list_of_common_words
        

def get_all_words(text):
    words = re.findall(r'[^\W|\d]+', text)
    return words


if __name__ == '__main__':
    number_of_output_words = 10
    filepath = input('Name of the file:')
    text_from_file = load_data(filepath)
    text_from_file.lower()
    list_of_common_words = get_most_frequent_words (text_from_file, number_of_output_words)
    print(str(number_of_output_words) + ' of the most common words: ')
    for number_of_word in range(number_of_output_words):
        print(list_of_common_words[number_of_word])