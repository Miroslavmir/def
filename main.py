# 1. Написать функцию для определения, является ли введённое число палиндромом.
# def is_palidrome(num):
#     if str(num) == str(num)[::-1]:
#         return True
#     else:
#         return False
# result = is_palidrome(12345)
# print(result)


# 2. Написать функцию, которая находит самую длинную подстроку,
# которая является префиксом среди массива строк. (Есть массив строк.
# Например, "Потолок" и "Полёт" и "попандопало". В данном случае, общая строка,
# с которой начинается каждая строка - "По".
# Т.е. это - самая максимальная подстрока, с которой начинается каждая строка массива).
# def get_longest_prefix(arr):
#     max_len = 0
#     for i in range(len(arr)):
#         if len(arr[i]) > max_len:
#             max_len = len(arr[i])
#             return max_len
# list = ['потолок', 'полёт','попандопало']
# result = get_longest_prefix(arr = list)
# print(result)
# 3. Написать функцию, которая определяет, правильно ли в строке расставлены скобки.
def is_balansed(str):

    if str.count('(') == str.count(')'):

        return True
    else:
        return False
print(is_balansed('())'))
