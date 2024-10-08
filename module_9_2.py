# Домашнее задание по теме "Списковые, словарные сборки"

first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

# В переменную first_result запишите список созданный при помощи сборки состоящий
# из длин строк списка first_strings, при условии, что длина строк не менее 5 символов.
first_result = [len(x) for x in first_strings if len(x) >= 5]
print(first_result)

# В переменную second_result запишите список созданный при помощи сборки состоящий из
# пар слов(кортежей) одинаковой длины. Каждое слово из списка first_strings должно
# сравниваться с каждым из second_strings. (два цикла)
second_result = [(a, b) for a in first_strings for b in second_strings if len(a) == len(b)]
print(second_result)

# В переменную third_result запишите словарь созданный при помощи сборки, где парой
# ключ-значение будет строка-длина строки. Значения строк будут перебираться из
# объединённых вместе списков first_strings и second_strings. Условие записи пары в
# словарь - чётная длина строки.
third_result = {z: len(z) for z in (first_strings + second_strings) if len(z) % 2 != 1}
print(third_result)