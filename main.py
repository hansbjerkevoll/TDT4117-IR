import data_loading_preprocessing
import dictionary_building

"""
    Task 1: Data loading and preprocessing
"""
paragraphs = data_loading_preprocessing.load_and_process_file("pg3300.txt")
processed_paragraphs = paragraphs[0]
original_paragraphs = paragraphs[1]

"""
    Task 2: Dictionary building
"""
dictionary_building.build_dictionary(processed_paragraphs)



