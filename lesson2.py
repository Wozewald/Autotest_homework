number_1 :int = 1
number_2 :int = 1

#Формулы сокращенного умножения
formula = number_1 * number_1 + 2 * number_1 * number_2 + number_2 * number_2

print(f"Умножение:{formula}")

if formula > 10:
    print("Больше 10")
else:
    print("10 или меньше")

