def single_root_words(root_word, *other_words):
    same_words = []
    for word in other_words:
        if (                  """ 1 """
                # str(root_word).lower() in str(word).lower()
                # or
                # str(word).lower() in str(root_word).lower()
                              """ 2 """
                str(root_word).lower().count(str(word).lower())
                or
                str(word).lower().count(str(root_word).lower())
        ):
            same_words.append(word)
    return same_words


print(single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies'))
# ['richiest', 'richies']

print(single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel'))
# ['Disable']
