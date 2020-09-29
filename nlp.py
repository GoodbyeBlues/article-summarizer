import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.corpus import stopwords
import nltk
import string

# recipe_doc = open('recipe_example.txt', r)  # Example recipe document
example_doc = 'Ingredients ingredients !are apples, bananas, and bread, bread and more bread.'
nltk.download('stopwords')
stopwords.words('english')


def main():
    create_text_reference(example_doc)

def create_text_reference(text):
    """ Create a compiler friendly reference of the user's article

    Keyword arguments
    example_doc -- the user supplied article
    Return: return_description
    """
    word_dict = {}
    # Let the list of unique words be == the user given text
    # (but remove all punctuation, whitespace, and make it all lower case so it's easy to compare)
    unique_words = example_doc.translate(str.maketrans('', '', string.punctuation)).lower().split()
    for idx, val in enumerate(unique_words):
        if val in word_dict:
            word_dict[val] += 1
        else:
            word_dict.update({unique_words[idx]:1})

    return word_dict

def determine_word_freq(word_dict, unique_words):
    """ Determine word frequency of the user's article

    Args: Takes text reference from create_text_reference()
    Returns:
    """
    word_freq_dict = {}
    unique_words_count = len(unique_words)

    for count, word in enumerate(word_dict):
        word_freq_dict[word] = count / float(unique_words_count)

    print(word_freq_dict)


if __name__ == '__main__':
    main()
