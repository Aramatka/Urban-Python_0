# Задача "Счётчик вызовов":
# Порой необходимо отслеживать, сколько раз вызывалась та или иная функция. К сожалению, 
# в Python не предусмотрен подсчёт вызовов автоматически.
# Давайте реализуем данную фишку самостоятельно!
# Вам необходимо написать 3 функции:
# Функция count_calls подсчитывающая вызовы остальных функций.
# Функция string_info принимает аргумент - строку и возвращает кортеж из: длины этой строки, 
# строку в верхнем регистре, строку в нижнем регистре.
# Функция is_contains принимает два аргумента: строку и список, и возвращает True, если строка находится
#  в этом списке, False - если отсутствует. Регистром строки при проверке пренебречь: UrbaN ~ URBAN.
# Пункты задачи:
# Создать переменную calls = 0 вне функций.
# Создать функцию count_calls и изменять в ней значение переменной calls. 
# Эта функция должна вызываться в остальных двух функциях.
# Создать функцию string_info с параметром string и реализовать логику работы по описанию.
# Создать функцию is_contains с двумя параметрами string и list_to_search, реализовать логику работы по описанию.
# Вызвать соответствующие функции string_info и is_contains произвольное кол-во раз 
# с произвольными данными.
# Вывести значение переменной calls на экран(в консоль).
calls = 0
def count_calls():
    global calls
    calls +=1
    return calls

count_calls()

def string_info ():
    global calls, count_calls
    count_calls()
    in_string = str(input('Введите строку: '))
    out_string= (len(in_string), in_string.upper(), in_string.lower())
    return out_string

def is_contains ():
    global calls, count_calls
    count_calls()
    string = "Urban"
    list_to_search = ("URaRban", "UrbaN")
    list_to_search_upper = [s.upper () for s in list_to_search]
    result = string.upper() in list_to_search_upper
    return result

print (string_info())   
print(is_contains())
print(is_contains())
print(calls)