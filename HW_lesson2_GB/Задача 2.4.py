# Задача № 4: Пользователь вводит строку из нескольких слов, разделённых пробелами.
#             Вывести каждое слово с новой строки. Строки нужно пронумеровать.
#             Если слово длинное, выводить только первые 10 букв в слове.
# Решение:

sentence = input('Введите предложение, разделив каждое слово пробелом: ')

# функция split() - это разделитель (по умолчанию разделителем является пробел)
# функция split() возвращает список, где каждый элемент это значение до разделителя
# пример: я учусь программированию --> функция вернет список = ['я', 'учусь', 'программированию']
my_list = sentence.split()

# количество итерации цикла for = количеству элементов в списке
for i in range(len(my_list)):
    # если длина элемента под индексом i имеет длину больше 10 символов, то с помощью среза выводим только 10 символов
    if (len(my_list[i]) > 10):
        # срез [0:10] означает то, что нужно выводить только строку от 0-го индекса до 10-го (не включительно)
        print(f'{i + 1}. {my_list[i][0:10]}')
    else:
        print(f'{i + 1}. {my_list[i]}')
