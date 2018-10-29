import gensim

"""
    Task 2: Dictionary building
        Remove stopwords and convert paragraphs into Bags-of-Words
"""


def build_dictionary(paragraphs):

    # 2.0 Build a dictionary
    dictionary = gensim.corpora.Dictionary(paragraphs)

    # 2.1 Filter out stopwords using a local file with stopwords
    stopwords = open("txt_files/common-english-words.txt", "r").readline().split(',')
    stopwords_id = [dictionary.token2id[stopword] for stopword in stopwords if stopword in dictionary.token2id]
    dictionary.filter_tokens(stopwords_id)

    # 2.2 Map paragraphs into Bags-Of-Words. A corpus object
    corpus = [dictionary.doc2bow(paragraph) for paragraph in paragraphs]
    return corpus, dictionary
