import random
import string
#from nltk.stem.porter import PorterStemmer

"""
Task 1: Data Loading and preprocessing
"""

# 1.0 random number generator
random.seed(123)


# 1.1 Reads the file from the txt_files dir.
# (No idea why they want us to use codecs.open(). Its outdated and bad. So I didn't)
file = open("txt_files/practice.txt", "r")

# 1.2 Partition file into seperate paragraphs
paragraph_list = list()
current_paragraph = list()

# Keep track of un-processed paragraphs. For displaying purposes
original_paragraph_list = list()
original_paragraph = ""

for line in file:
    original_line = line

    # 1.5 Remove string punctuation, whitespace and convert to lower case
    line = ''.join(char for char in line if char not in set(string.punctuation)).strip().lower()

    # 1.4 Tokenize paragraphs (split them into a list of words, need to make sure each paragraph is one-dimensional)
    if len(line.split()) != 0:
        current_paragraph += line.split(' ')
        original_paragraph += original_line

    # 1.6 Using PorterStemmer to stem words
    #for word in current_paragraph:
        #current_paragraph.replace(word, PorterStemmer().stem(word))

    if line == "" and len(current_paragraph) != 0:
        # 1.3 Filter out paragraphs containing "Gutenberg"
        if 'gutenberg' not in current_paragraph:
            paragraph_list.append(current_paragraph)
            original_paragraph_list.append(original_paragraph)
        current_paragraph = list()
        original_paragraph = ""

print(paragraph_list)
print(len(paragraph_list))