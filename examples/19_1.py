# Тип №19
# Задание №27811
# Задания для самопроверки: №27805, 27808

def f(x, h):
    if x >= 48 and h == 2:
        return 1
    if x >= 48 and h < 2:
        return 0
    if x < 48 and h == 2:
        return 0
    if x < 48 and h < 2:
        if h % 2 == 0:
            return f(x + 1, h + 1) or f(x + 4, h + 1) or f(x * 2, h + 1)
        else:
            return f(x + 1, h + 1) or f(x + 4, h + 1) or f(x * 2, h + 1)
        
for s in range(1, 48):
    if f(s, 0):
        print("Ответ на задание:", s)
        break