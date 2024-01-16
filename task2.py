# В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых.
# Не учитывать знаки препинания и регистр символов.
# За основу возьмите любую статью из википедии или из документации к языку.

text = ''
text = text.lower().split()
words = []
for word in text:
    words.append(word.strip('".:,()-—!?'))
# print(words)

word_count = {}
for word in words:
  if word in word_count:
    word_count[word] += 1
  else:
    word_count[word] = 1
sort_word_count = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
for word, count in sort_word_count[:10]:
  print(f'{word}: {count}')