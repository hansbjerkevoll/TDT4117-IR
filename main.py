import data_loading_preprocessing
import dictionary_building
from retrieval_models import retrieval_models
import gensim

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
retrieved = retrieval_models(corpus, dictionary)
tfidf_index = retrieved[0]
lsi_index = retrieved[1]


"""
    Task 4: Querying
"""
#4.1
text_query  = "What is the function nation of money?"
query = data_loading_preprocessing.process_query(text_query)
query_corpus = dictionary.doc2bow(query)
query_collection = [query_corpus]

#4.2 convert BOW to TF-IDF representation
tfidf_model = gensim.models.TfidfModel(query_collection)
print(tfidf_model)
tfidf_query = tfidf_model[query_collection]

#4.3
doc2similarity = enumerate(tfidf_index[tfidf_query])
print(sorted(doc2similarity, key=lambda kv: -kv[1])[:3])


#4.4
lsi_model = gensim.models.LsiModel(query_corpus, id2word=dictionary, num_topics=100)
lsi_query = lsi_model[tfidf_query]

print( sorted(lsi_query, key=lambda kv: -abs(kv[1]))[:3] )
#print( lsi.show_topics() )
doc2similarity = enumerate(lsi_index[lsi_query])
print( sorted(doc2similarity, key=lambda kv: -kv[1])[:3] )

