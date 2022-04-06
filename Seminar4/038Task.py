# 38.	Напишите программу, удаляющую из текста все слова содержащие "абв".
line = 'Это абв тестовый абв текст абв для абв примера абв'.split(' ')
fragment = 'абв'
new_words = []
for word in line:
    if fragment not in word:
        new_words.append(word)
print(line)
print(' '.join(new_words))