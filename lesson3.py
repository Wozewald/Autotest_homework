# Первое
first_list = [10, 15, 30, 70, 150]

n_elem = first_list[2]

print(n_elem)

x_elem = first_list
x_elem += [40]

print(x_elem)


# Второе

first_tuple = ('красный', 'зеленый', 'синий')

n_tuple = first_tuple[2]
print(n_tuple)

x_tuple = n_tuple
#x_tuple[1] = 'бордовый'

lust_tuple = first_tuple
print(first_tuple)
print(lust_tuple)


# Третье

first_set = {1, 2, 3, 4, 5,}
lust_set = {1, 3, 4, 6}

common = first_set.intersection(lust_set)
print(common)

union = first_set.union(lust_set)
print(union)

lust_set.discard(3)

print(first_set)
print(lust_set)

# Четвертое

first_dict = {
    "Имя":"Алексей",
    "Курс": 2,
    "Город":"Москва"
}

print(first_dict.get("Имя"))

first_dict.update({"Учится":"ДА"})

del first_dict["Курс"]

print(first_dict)

