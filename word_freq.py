"""
Программа считает Топ-100 слов для переданного ей текстого файла.

Путь до текстового файла передается программе в виде аргумента
В выводе не должно быть стоп-слов (междометий, союзов, местоимений и т.д.)
Список стоп-слов можно взять из популярного пакета nltk

Тебе может понадобится модуль os, модуль argparse, цикл и словарь
"""
import re
import string

count = 0
frequency = {}
stopwords = []

doc = open('test.txt', 'r')
text = doc.read().lower()

match_pattern = re.findall(r'\b[a-z]{3,20}\b', text)
 
for word in match_pattern:
    count = frequency.get(word,0)
    frequency[word] = count + 1
 
list_frequency = list(frequency.items())
list_frequency.sort(key=lambda words: words[1])

for words in reversed(list_frequency):
    print(f" {count} - {words[0]} : {words[1]}")
    count += 1
    if count > 100:
        break

doc.close()