import random
import string
from nltk.stem.porter import PorterStemmer


"""
    Task 1: Data Loading and preprocessing
        Load and process (clean, tokenize and stem) data
"""

def load_and_process_file(filename):

    # 1.0 random number generator
    # (Don't know why we need to do this, probably for later use)
    # (This is irrelevant in this file, but will keep it because the assignment says so. #goodstudent)
    random.seed(123)

    # 1.1 Reads the file from the txt_files dir.
    # (No idea why they want us to use codecs.open(). Its outdated and bad. So I didn't)
    file = open("txt_files/" + filename, "r")

    # 1.2 Partition file into seperate paragraphs
    paragraph_list = list()
    current_paragraph = list()

    # Keep track of un-processed paragraphs. For displaying purposes
    original_paragraph_list = list()
    original_paragraph = ""

    # 1.6 PorterStemmer
    stemmer = PorterStemmer()

    for line in file:

        original_line = line

        # 1.5 Remove string punctuation, whitespace and convert to lower case
        line = ''.join(char for char in line if char not in set(string.punctuation)).strip().lower()

        # 1.4 Tokenize paragraphs (split them into a list of words, need to make sure each paragraph is one-dimensional)
        if len(line.split()) != 0:
            current_paragraph += line.split(' ')
            original_paragraph += original_line

        if line == "" and len(current_paragraph) != 0:
            # 1.3 Filter out paragraphs containing "Gutenberg"
            """
            guten_check = False
            for word in current_paragraph:
                if 'gutenberg' in word:
                    guten_check = True
            """
            if "gutenberg" not in current_paragraph:

                # 1.6 Using PorterStemmer to stem words
                for i, word in enumerate(current_paragraph):
                    current_paragraph[i] = stemmer.stem(word)

                paragraph_list.append(current_paragraph)
                original_paragraph_list.append(original_paragraph)

            current_paragraph = list()
            original_paragraph = ""

    return paragraph_list, original_paragraph_list


"""
    Task 4.1 Process the query
"""


def process_query(query_string):

    query_string = ''.join(char for char in query_string if char not in set(string.punctuation)).strip().lower()
    query_list = query_string.split(' ')
    for i, word in enumerate(query_list):
        query_list[i] = PorterStemmer().stem(word)

    return query_list
