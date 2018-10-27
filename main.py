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

indexes = retrieval_models(corpus, dictionary)
tfidf_index = indexes[0]
lsi_index = indexes[1]


"""
    Task 4: Querying
"""

text_query = "What is the function of money?"
print(data_loading_preprocessing.process_query(text_query))

#4.1
text_query  = "What is the function of money?"
query = data_loading_preprocessing.process_query(text_query)
query = dictionary.doc2bow(query)

#4.2 convert BOW to TF-IDF representation

tfidf_query = tfidf_model[]


doc2similarity = enumerate(tfidf_index[tfidf_query])
