import gensim


def retrieval_models(corpus, dictionary):

    # 3.1 Build TF-IDF model using corpus
    tfidf_model = gensim.models.TfidfModel(corpus)

    # 3.2 Map Bags-of-Words into TF-IDF weights
    tfidf_corpus = tfidf_model[corpus]

    # 3.3 Construct MatrixSimilarity object
    index_tfidf = gensim.similarities.MatrixSimilarity(tfidf_corpus)

    # 3.4 Repeat the above procedure for LSI model using as an input the corpus with TF-IDF weights
    lsi_model = gensim.models.LsiModel(tfidf_corpus, id2word=dictionary, num_topics=100)
    lsi_corpus = lsi_model[corpus]
    index_lsi = gensim.similarities.MatrixSimilarity(lsi_corpus)

    # 3.5 Report (print) and try to interpret first 3 LSI topics
    #print(lsi_model.show_topics())

    return index_tfidf, tfidf_model
