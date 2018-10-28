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
tfidf_model = retrieved[1]

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

for sim in simimilarities:
    para_index = sim[0]
    para = original_paragraphs[para_index].strip().split('\n')[0:5]
    report_string = ("[paragraph " + str(para_index + 1) + "]\n" + ''.join(line + '\n' for line in para))
    print(report_string)

"""
# 4.4
lsi_model = gensim.models.LsiModel(query_corpus, id2word=dictionary, num_topics=100)
lsi_query = lsi_model[tfidf_query]

print( sorted(lsi_query, key=lambda kv: -abs(kv[1]))[:3] )
#print( lsi.show_topics() )
doc2similarity = enumerate(lsi_index[lsi_query])
print( sorted(doc2similarity, key=lambda kv: -kv[1])[:3] )
"""
