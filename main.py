import data_loading_preprocessing
import dictionary_building
from retrieval_models import retrieval_models

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
        Query the models built in the previous part, and report results
"""
# 4.1 Apply  all  necessary transformations
text_query = "What is the function of money?"
query = data_loading_preprocessing.process_query(text_query)
query_corpus = dictionary.doc2bow(query)

# 4.2 Convert BOW to TF-IDF representation
tfidf_query = tfidf_model[query_corpus]

# 4.3 Report (print) top 3 the most relevant paragraphs for the query "What is the function of money?"
similarities = sorted(enumerate(tfidf_index[tfidf_query]), key=lambda item: -item[1])[:3]
report_string = "\nTop 3 Matching Paragraphs:\n"
for sim in similarities:
    para_index = sim[0]
    para = original_paragraphs[para_index].strip().split('\n')[0:5]
    report_string += ("[paragraph " + str(para_index + 1) + "]\n" + ''.join(line + '\n' for line in para)) + '\n'
report_string = report_string.rstrip()
print(report_string)


# 4.4 Convert query TF-IDF representation into LSI-topics representation
lsi_query = lsi_model[tfidf_query]
lsi_topic_similarities = sorted(lsi_query, key=lambda item: -abs(item[1]))[:3]
topics = lsi_model.show_topics()

# 4.4.1 Report (print) top 3 topics
lsi_topic_report = "\nTop 3 Matching Topics:\n"
for sim in lsi_topic_similarities:
    topic_index = sim[0]
    lsi_topic_report += ("[topic " + str(topic_index + 1) + "]\n" + str(topics[topic_index][1]) + '\n\n')
lsi_topic_report = lsi_topic_report.rstrip()
print(lsi_topic_report)

# 4.4.2 Report (print) top 3 most relevant documents
doc2similarity = enumerate(lsi_index[lsi_query])
lsi_doc_similarities = sorted(doc2similarity, key=lambda item: -item[1])[:3]
lsi_doc_report = "\nTop 3 Matching Paragraphs (LSI):\n"
for sim in lsi_doc_similarities:
    para_index = sim[0]
    para = original_paragraphs[para_index].strip().split('\n')[0:5]
    lsi_doc_report += ("[paragraph " + str(para_index + 1) + "]\n" + ''.join(line + '\n' for line in para)) + '\n'
lsi_doc_report = lsi_doc_report.rstrip()
print(lsi_doc_report)
