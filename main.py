import data_loading_preprocessing
import dictionary_building
from retrieval_models import retrieval_models

"""
    Task 1: Data loading and preprocessing
"""
paragraphs = data_loading_preprocessing.load_and_process_file("practice.txt")
processed_paragraphs = paragraphs[0]
original_paragraphs = paragraphs[1]

"""
    Task 2: Dictionary building
"""
things = dictionary_building.build_dictionary(processed_paragraphs)
corpus = things[0]
dictionary = things[1]


"""
    Task 3: Retrieval Models

"""
blah = retrieval_models(corpus, dictionary)
firstblah = blah[0]
firstbljde = blah[1]


"""
    Task 4: Querying
"""

text_query = "What is the function of money?"
print(data_loading_preprocessing.process_query(text_query))

