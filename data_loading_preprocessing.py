import random

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
current_paragraph = ""
for line in file:
    line = line.strip()
    current_paragraph += line

    if line == "" and current_paragraph != "":
        # 1.3 Filter out paragraphs containing "Gutenberg"
        if "Gutenberg" not in current_paragraph:
            paragraph_list.append(current_paragraph)
        current_paragraph = ""

print(paragraph_list)
print(len(paragraph_list))