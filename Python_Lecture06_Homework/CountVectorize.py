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
            ValueError('"strings" are not Iterable')
        for string in strings:
            if not isinstance(string, str):
                ValueError('"strings" don\'t consist of strings')

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
            ValueError('"strings" are not Iterable')
        for string in strings:
            if not isinstance(string, str):
                ValueError('"strings" don\'t consist of strings')

        all_words = []
        for string in strings:
            words = string.split()
            for word in words:
                all_words.append(word.lower())
        self.feature_names = set(all_words)


if __name__ == "__main__":
    corpus = [
        "Crock Pot Pasta Never boil pasta again",
        "Pasta Pomodoro Fresh ingredients Parmesan to taste",
    ]

    vectorizer = CountVectorizer()
    count_matrix = vectorizer.fit_transform(corpus)
    print(vectorizer.get_feature_names())
    print(count_matrix)
