
#  Напишите функцию-генератор all_variants(text), которая принимает строку text и возвращает объект-генератор, при каждой итерации которого будет возвращаться подпоследовательности переданной строки.
#
# Пункты задачи:
# Напишите функцию-генератор all_variants(text).
# Опишите логику работы внутри функции all_variants.
#  Вызовите функцию all_variants и выполните итерации.

def all_variants(text):
    for i in range(len(text)):
        for j in range(len(text)-i):
            yield text[j: j+i+1]


a = all_variants("abc")
for i in a:
    print(i)



