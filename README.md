# Duplicate Question Detection
This project aims to detect duplicate questions using a machine learning approach. The notebook includes data processing, text preprocessing, and feature engineering steps to build a model that can identify duplicate questions.


## Features

- Data loading and inspection
- Data preprocessing and cleaning
- Text preprocessing
- Feature engineering
- Model training and evaluation
- Visualizations of results

## Feature engineering

- cwc_min: This feature measures the ratio of the number of common words between the two questions to the length of the smaller question. It helps to quantify the overlap of vocabulary in relation to the size of the smaller question.
- cwc_max: This feature measures the ratio of the number of common words to the length of the larger question. It captures how common words relate to the size of the larger question.
- csc_min: This feature calculates the ratio of the number of common stop words to the smaller stop word count between the two questions. It reflects the overlap of common stop words relative to the size of the smaller question.
- csc_max: This feature measures the ratio of the number of common stop words to the larger stop word count. It provides insight into how common stop words compare to the size of the larger question.
- ctc_min: This feature is the ratio of the number of common tokens (words or phrases) to the smaller token count among the two questions. It indicates the overlap of tokens in relation to the size of the smaller question.
- ctc_max: This feature measures the ratio of the number of common tokens to the larger token count. It shows how common tokens relate to the size of the larger question.
- last_word_eq: This feature indicates whether the last word in both questions is the same. It is represented as 1 if the last words match and 0 if they do not.
- first_word_eq: This feature indicates whether the first word in both questions is the same. It is represented as 1 if the first words match and 0 if they do not.
- mean_len: This feature is the average length of the two questions measured in number of words. It provides a general sense of the length of both questions combined.
- abs_len_diff: This feature represents the absolute difference in the length of the two questions measured in number of words. It quantifies how different the two questions are in terms of length.
- longest_substr_ratio: This feature measures the ratio of the length of the longest common substring between the two questions to the length of the smaller question. It reflects the similarity of the two questions based on the longest continuous sequence of matching characters.
- q1_len: The length of the first question measured in number of words.
- q2_len: The length of the second question measured in number of words.
- q1_num_words: The number of words in the first question.
- q2_num_words: The number of words in the second question.
- word_common: The total number of common words between the two questions.
  word_total: The total number of unique words across both questions.


Try Here :
https://quora-question-pair.streamlit.app/
