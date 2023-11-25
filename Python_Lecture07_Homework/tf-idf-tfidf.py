from math import log
from typing import Iterable


class CountVectorizer:
    def __init__(self):
        self.feature_names = None
        self.document_term_matrix = None

    def fit_transform(self, strings: Iterable[str]) -> Iterable[Iterable[int]]:
        """
        Set feature names and generate document-term matrix

        :param: strings for processing
        :return: document-term matrix
        """
        if not isinstance(strings, Iterable):
            ValueError("'strings' are not Iterable")
        for string in strings:
            if not isinstance(string, str):
                ValueError("'strings' don't consist of strings")

        self.set_feature_names(strings)
        self.document_term_matrix = []
        for string in strings:
            words = string.split()
            counter = {feature_name: 0 for feature_name in self.feature_names}
            for word in words:
                counter[word.lower()] += 1
            self.document_term_matrix.append(list(counter.values()))
        return self.document_term_matrix

    def get_feature_names(self) -> Iterable[str]:
        """
        Return feature names

        :return: feature names
        """
        return self.feature_names

    def set_feature_names(self, strings: Iterable[str]) -> None:
        """
        Fill feature names
        """
        if not isinstance(strings, Iterable):
            ValueError("'strings' are not Iterable")
        for string in strings:
            if not isinstance(string, str):
                ValueError("'strings' don't consist of strings")

        all_words = []
        for string in strings:
            words = string.split()
            for word in words:
                all_words.append(word.lower())
        self.feature_names = set(all_words)


def tf_transform(matrix: Iterable[Iterable[int]]) -> Iterable[Iterable[int]]:
    """
    Generate tf-matrix based on matrix

    :return: tf-matrix
    """
    if not isinstance(matrix, Iterable):
        ValueError("'matrix' are not Iterable")
    for row in matrix:
        if not isinstance(row, Iterable):
            ValueError("'row' in 'matrix' is not Iterable")

    tf_matrix = []

    for row in matrix:
        tf_matrix.append([])
        row_sum = 0
        for cell in row:
            row_sum += cell
        for cell in row:
            tf_matrix[-1].append(tf_function(cell, row_sum))

    return tf_matrix


def tf_function(repeats: int, total_words_in_row: int) -> float:
    """Calculates value of tf-metric"""
    return round(repeats / total_words_in_row, 3)


def idf_transform(matrix: Iterable[Iterable[int]]) -> Iterable[Iterable[int]]:
    """
    Generate idf-matrix based on matrix

    :return: idf-matrix
    """
    if not isinstance(matrix, Iterable):
        ValueError("'matrix' are not Iterable")
    for row in matrix:
        if not isinstance(row, Iterable):
            ValueError("'row' in 'matrix' is not Iterable")

    if len(matrix) == 0:
        return []

    idf_matrix = [0 for x in matrix[0]]
    number_of_rows = len(matrix)
    for i, cell in enumerate(idf_matrix):
        number_of_documents_with_word = 0
        for row in matrix:
            if row[i] > 0:
                number_of_documents_with_word += 1

        idf_matrix[i] = idf_function(number_of_rows, number_of_documents_with_word)

    return idf_matrix


def idf_function(number_of_documents: int, number_of_documents_with_word: int) -> float:
    """Calculates value of idf-metric"""
    return round(
        log((number_of_documents + 1) / (number_of_documents_with_word + 1)) + 1, 1
    )


class TfidfTransformer:
    def fit_transform(self, matrix: Iterable[Iterable[int]]) -> Iterable[Iterable[int]]:
        """
        Generate tfidf-matrix based on matrix

        :return: tfidf-matrix
        """
        tf_matrix = tf_transform(matrix)
        idf_matrix = idf_transform(matrix)

        tfidf_matrix = []
        for row in tf_matrix:
            tfidf_matrix.append([])
            for i, cell in enumerate(row):
                tfidf_matrix[-1].append(round(row[i] * idf_matrix[i], 3))
        return tfidf_matrix


class TfidfVectorizer(CountVectorizer):
    def __init__(self):
        super().__init__()

    def fit_transform(self, strings: Iterable[str]) -> Iterable[Iterable[int]]:
        """
        Generate tfidf-matrix based on strings

        :return: tfidf-matrix
        """
        count_matrix = super().fit_transform(strings)
        tfidf_transformer = TfidfTransformer()
        return tfidf_transformer.fit_transform(count_matrix)


if __name__ == "__main__":
    corpus = [
        "Crock Pot Pasta Never boil pasta again",
        "Pasta Pomodoro Fresh ingredients Parmesan to taste",
    ]

    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(corpus)
    print(vectorizer.get_feature_names())
    print(tfidf_matrix)

    # To test tasks №1 - №4
    # vectorizer = CountVectorizer()
    # count_matrix = vectorizer.fit_transform(corpus)
    # print(vectorizer.get_feature_names())
    # print(count_matrix)
    # tf_matrix = tf_transform(count_matrix)
    # print(tf_matrix)
    # idf_matrix = idf_transform(count_matrix)
    # print(idf_matrix)
    # transformer = TfidfTransformer()
    # tfidf_matrix = transformer.fit_transform(count_matrix)
    # print(tfidf_matrix)
