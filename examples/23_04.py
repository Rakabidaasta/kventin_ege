# Тип №23. Количество программ с обязательным и избегаемым этапами
# Задание №
# Задания для самопроверки: №

# Это задание по сути совмещает в себе примеры из 23_02.py и 23_03.py

# Исполнитель Фибо преобразует число на экране.
# У исполнителя есть две команды, которым присвоены номера:
def f(start, end):
    if start == end:
        return 1

    if start > end:
        return 0

    if start == 15:
        return 0
    
    # 1.  Прибавить 1
    # 2.  Прибавить 2
    return f(start + 1, end) + f(start + 2, end)

# Сколько существует программ, которые преобразуют исходное число 3 в число 20 и при этом траектория вычислений содержит число 9 и не содержит числа 15?
print(f(3, 9) * f(9, 20))