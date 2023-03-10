# Требуется реализовать функцию longest_words(file), 
# которая выводит слово, имеющее максимальную длину (или список слов, если таковых несколько).
import os.path
def longest_words(file):
    with open('article.txt', 'r', encoding='utf-8') as text:
        words = text.read().split()
        max_length = len(max(words, key=len))
        sought_words = [word for word in words if len(word) == max_length]
        if len(sought_words) == 1:
            return sought_words[0]
        return sought_words
 
print(longest_words('article.txt'))