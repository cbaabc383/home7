# Задача 34: Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. 
# Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает, 
# Вам стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов 
# (т.е. число гласных букв) в каждой фразе стихотворения одинаковое. 
# Фраза может состоять из одного слова, если во фразе несколько слов, 
# то они разделяются дефисами. Фразы отделяются друг от друга пробелами. 
# Стихотворение Винни-Пух вбивает в программу с клавиатуры. 
# В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, 
# если с ритмом все не в порядке
# Ввод:
# пара-ра-рам рам-пам-папам па-ра-па-дам
# Вывод:
# Парам пам-пам

vovels = set('аеёиоуыэюя')

poem = input('Напишите стих Вини-Пуха: ').lower()
phrase = poem.split()
# print(phrase)
signal = set()

for i in range(len(phrase)):
    count = 0
    for letter in phrase[i]:
        if letter in vovels:
            count += 1
    # print(count)
    signal.add(count)
# print(signal)
# print(len(signal))
if len(signal) > 1:
    print('Пам парам')
else:
    print('Парам пам-пам')    

