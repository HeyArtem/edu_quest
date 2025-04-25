# my_list = []
# my_list2 = (1, 2, 3, 4, 5)
# my_list3 = [1, 2, 3, 4, 5]
#
# my_list.append(111)
# my_list3.insert(2, 666)
# my_list3.extend([7, 8])
#
#
# del my_list3[2]
# my_list3.remove(5)
# print(my_list, my_list3)
# z = my_list3.pop(0)
# print(my_list3, z)
#
# my_list3.clear()
# print(my_list3)
# del my_list

nums = [1, 5, 20, 5, 2, 3, 4, 5]
new_list = [i for i in nums if i != 5]
print(new_list)

# Сортировка по убыванию
nums.sort(reverse=True)  # Метод sort()
sorted_nums = sorted(nums, reverse=True)  # Функция sorted()


# # Перевод строк в верхний регистр
# # (У списка нет .upper(), это у строк!)
# words = [word.upper() for word in words]  # List comprehension
#
# for i in range(len(words)):
#     words[i] = words[i].upper()  # Через for
#
#
# # Найти второй по величине элемент (Сложно, но ты справишься!)
# nums.remove(max(nums))  # Удаляем самый большой
# second_max = max(nums)  # Ищем новый максимум

# Без set() и встроенных функций, кроме max()

nums = [2, 100, 34, 77, 32, 1, 444, 98, 999, 4444]
first_max = max(nums)  # Находим самое большое число
second_max = float("-inf")  # Задаём очень маленькое значение

for num in nums:
    if num > second_max and num != first_max:
        second_max = num  # Обновляем второе по величине число
print(second_max)
