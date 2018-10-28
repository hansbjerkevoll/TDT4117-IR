import data_loading_preprocessing
import dictionary_building
from retrieval_models import retrieval_models
import gensim

"""
    Task 1: Data loading and preprocessing
"""
paragraphs = data_loading_preprocessing.load_and_process_file("pg3300.txt")
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
tfidf_model = retrieved[1]
lsi_index = retrieved[2]
lsi_model = retrieved[3]

"""
    Task 4: Querying
"""
# 4.1 Apply  all  necessary transformations
text_query = "How taxes influence Economics?"
query = data_loading_preprocessing.process_query(text_query)
query_corpus = dictionary.doc2bow(query)

# 4.2 Convert BOW to TF-IDF representation
query_tfidf = tfidf_model[query_corpus]

# 4.3 Report (print) top 3 the most relevant paragraphs for the query "What is the function of money?"
simimilarities = sorted(enumerate(tfidf_index[query_tfidf]), key=lambda item: -item[1])[:3]
report_string = ""
for sim in simimilarities:
    para_index = sim[0]
    para = original_paragraphs[para_index].strip().split('\n')[0:5]
    report_string += ("[paragraph " + str(para_index + 1) + "]\n" + ''.join(line + '\n' for line in para))
    report_string += "\n"

#print(report_string.rstrip())


# 4.4
lsi_query = lsi_model[query_tfidf]
lsi_similarities = sorted(lsi_query, key=lambda kv: -abs(kv[1]))[:3]
print(lsi_similarities)
topics = lsi_model.show_topics()

for topic in topics:
    print(topic)
lsi_report = ""
for sim in lsi_similarities:
    topic_index = sim[0]
    print(topic_index+1)

doc2similarity = enumerate(lsi_index[lsi_query])
print(sorted(doc2similarity, key=lambda item: -item[1])[:3])

