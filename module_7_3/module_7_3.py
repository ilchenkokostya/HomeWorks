class WordsFinder:
    def __init__(self, *files):
        self.files = files

    def get_all_words(self):
        all_words = {}
        for file_name in self.files:
            with open(file_name, 'r', encoding='utf-8') as f:
                all_words[file_name] = f.read().split()
        return all_words

    def find(self, word):
        pass

    def count(self, word):
        pass


if __name__ == '__main__':
    finder2 = WordsFinder('test_file.txt')
    print(finder2.get_all_words())  # Все слова
    print(finder2.find('TEXT'))  # 3 слово по счёту
    print(finder2.count('teXT'))  # 4 слова teXT в тексте всего
