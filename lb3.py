
list_test = [15, 48, 59, 12, 340, 125]
tuple_test = (15, 48, 59, 12, 340, 125)
print(type(list_test))
print(type(tuple_test))
print("ID до изменений:   ",id(list_test))
list_test[3] = 10
print("ID после изменений:",id(list_test))
print("-------------------------------------")
print("ID до изменений:   ",id(tuple_test))
tuple_test = (15, 48, 59, 12, 341, 125)
print("ID после изменений:",id(tuple_test))

list_test = [5, 3, 5, 7, 3, 9, 1, 5, 8, 2, 7, 4]
set_test = set(list_test)
print("Число элементов в списке:", len(list_test))
print("Число эелементов во множестве:", len(set_test))
print(list_test, set_test)

import timeit

def check_present_in_list():
    return pres in list_test

def check_present_in_set():
    return pres in set_test

def check_absent_in_list():
    return miss in list_test

def check_absent_in_set():
    return miss in set_test

list_test = [i for i in range(1,100)]
set_test = set(list_test)

miss = -1
pres = 50

t1 = timeit.timeit(check_present_in_list, number=10000)
t2 = timeit.timeit(check_present_in_set,  number=10000)
t3 = timeit.timeit(check_absent_in_list,  number=10000)
t4 = timeit.timeit(check_absent_in_set,   number=10000)

print("  list есть:", t1)
print("  set  есть:", t2)
print("  list нет: ", t3)
print("  set  нет: ", t4)


import sys

dict_test = {
    1: "Анна",
    2: "Борис",
    3: "Вера",
    4: "Глеб",
    5: "Дина",
    6: "Егор",
    7: "Жанна",
    8: "Зоя",
    9: "Иван",
    10: "Кира",
}

print("Значение по ключу 6:", dict_test[6])

ids = list(range(1, 11))
list_test = ids
tuple_test = tuple(ids)
set_test = set(ids)
print("Размеры контейнеров по sys.getsizeof():")
print("list :", sys.getsizeof(list_test))
print("tuple:", sys.getsizeof(tuple_test))
print("set  :", sys.getsizeof(set_test))
print("dict :", sys.getsizeof(dict_test))





tupl = ("15", "2023.11.05", "Сидоров")
lst = [1001, 1002, 1003, 1004, 1005, 1006]
st = {1001, 1002, 1003, 1004}
dct = {
    1001: "ул. Ленина, 1",
    1002: "ул. Пушкина, 2",
    1003: "ул. Гоголя, 3",
    1004: "ул. Чехова, 4",
    1005: "ул. Толстого, 5",
    1006: "ул. Достоевского, 6"
}
print(f"Маршрут: №{tupl[0]}, {tupl[1]}, курьер {tupl[2]}")
print("Заказы в порядке создания:", *lst)
print("Доставленные заказы:", *st)
addresses_str = "; ".join(f"{k} - {v}" for k, v in dct.items())
print("Адреса заказов:", addresses_str)
print("")
a = 1007
lst.append(a)
print("После добавления заказа:",*lst)
n = 1003
if n in st:
    print(f"Заказ {n} доставлен: да")
else:
    print(f"Заказ {n} доставлен: нет")
b = 1005
print(f"Адрес заказа {b}:", dct[b])