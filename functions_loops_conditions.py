#Задача #1: множественная форма числительных

def plural_form(*args):
    #in_number, in_noun, form2, form3
    """Согласование окончаний существительных
           :param in_number: число
           :param in_noun: существительное, форма слова 1
           :param form2: форма слова 2
           :param form3: форма слова 3
    """
    # заканчивается на 1: именительный падеж
    # заканчивается на 2, 3 и 4: родительный падеж
    # заканчивается на 5, 6, 7, 8, 9, 0: множественная форма, родительный падеж
    # 11, 12, 13, 14 - есть особенность

    in_number = str(args[0])

    # родительный падеж
    list_genitive = ['2', '3', '4']

    fin_number = str(in_number)
    if len(fin_number) > 1:  #взять 2 последние 2 цифры
        fin_number = fin_number[-2:]
        if int(fin_number) < 1 or int(fin_number) > 19:
            fin_number = fin_number[-1]  #взять 1 последнюю цифру
    else:  #взять 1 последнюю цифру
        fin_number = fin_number[-1]

    version = 3 # по умолчанию - множественная форма, родительный падеж

    if fin_number == '1':
       #именительный падеж
       version = 1
    elif fin_number in list_genitive:
        #родительный падеж
        version = 2

    return f'{in_number} {args[version]}'


print(plural_form(1, 'яблоко', 'яблока', 'яблок'))
print(plural_form(2, 'яблоко', 'яблока', 'яблок'))
print(plural_form(11, 'студент', 'студента', 'студентов'))
print(plural_form(15, 'студент', 'студента', 'студентов'))
print(plural_form(3, 'студент', 'студента', 'студентов'), '\n')


#Задача #2: FizzBuzz

sum = 0
for i in range(1000, 20001):
    if i % 15 == 0:
        sum += i

print('Сумма чисел в диапазоне от 1000 до 20000 включительно, которые делятся и на 3 и на 5:', sum, '\n')

#Задача #3: Последовательность Фибоначчи

fib_prev = 1
fib_next = 1
i = 0
sum = 0
count = 1
list_even = []

while i < 10000000:
    i = fib_prev + fib_next
    count += 1  # количество всех элементов

    if i < 10000000:
        if i % 2 == 0:
            list_even.append(i)
            sum += i #сумма всех четных элементов

        fib_prev = fib_next
        fib_next = i


print('количество всех элементов = ', count)
print('сумма всех четных элементов = ', sum)
print('четные элементы: \n', list_even)
print('предпоследний элемент последовательности = ', fib_prev)

