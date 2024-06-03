# Домашняя работа по уроку "Пространство имен и способы вызова функции"

def single_root_words(root_word, *other_words):
    same_words = [] # создаем пустой список для слов
    for word in other_words: # проверяем, содержится ли слово в root_words
        if root_word in word or word in root_word:
            same_words.append(word)
    return same_words


result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)