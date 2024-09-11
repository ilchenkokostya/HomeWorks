class WordsFinder:
    def __init__(self, *files):
        self.files = files

    @staticmethod
    def remove_punctuation(text):
        for punc in [',', '.', '=', '!', '?', ';', ':', ' - ']:
            if punc in text:
                text = text.replace(punc, ' ')
        return text.strip()

    def get_all_words(self):
        all_words = {}
        for file_name in self.files:
            with open(file_name, 'r', encoding='utf-8') as f:
                all_words[file_name] = self.remove_punctuation(f.read()).lower().split()
        return all_words

    def find(self, word):
        find_word = {}
        for name, words in self.get_all_words().items():
            find_word[name] = [i for i, x in enumerate(words, 1) if x == word.lower()]
        return find_word

    def count(self, word):
        find_count = {}
        for name, values in self.find(word).items():
            find_count[name] = len(values)
        return find_count


if __name__ == '__main__':
    finder2 = WordsFinder('test_file.txt', 'test_file2.txt')
    print(finder2.get_all_words())  # Все слова
    print(finder2.find('TEXT'))  # 3 слово по счёту
    print(finder2.count('teXT'))  # 4 слова teXT в тексте всего
