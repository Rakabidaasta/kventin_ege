# В условии if у нас всегда проверка на истину
# Истина -- это True, положительное число, не пустая строка
# Ложь -- это False, неположительное число, пустая строка

if "":
    print("1")

if "a":
    print("2")

if 0:
    print("3")

if 10:
    print("4")

if True:
    print("5")

if False:
    print("6")

if not True:
    print("7")

if not False:
    print("8")


# Выведет 2458
print("x y w z")
for x in range(2):
    for y in range(2):
        for w in range(2):
            for z in range(2):
                if not ((x and (not y)) or (y == z) or (not w)):
                    print(x, y, z, w, ((x and (not y)) or (y == z) or (not w)))

print("x y w z 1 2")
for x in range(2):
    for y in range(2):
        for w in range(2):
            for z in range(2):
                f1 = int((x <= y) == (w or (not z)))
                f2 = int((x <= y) and ((not w) == z))
                if f2 == 0 and z == 1:
                    print(x, y, w, z, f1, f2)

# Если известные столбцы могут принести полезную информацию, благодаря которой мы отфильтруем, то их оставляем до фильтрации
# Иначе (даже если их значение не известно), то мы их удаляем, нам на них пофиг, они бесполезные
                    
print("x y z")
for x in range(2):
    for y in range(2):
        for z in range(2):
            f1 = int((x or y) <= (z == x))
            if f1 == 0:
                print(x, y, z)

print("x y w z")
for x in range(2):
    for y in range(2):
        for w in range(2):
            for z in range(2):
                f = int((w <= (y == z)) and (y == (z <= x)))
                if f == 0 and z == 0 and w == 0:
                    print(x, y, w, z, f)
n = 201
max1 = 0

while True:
    s = "1" * n

    while "1111" in s:
        s = s.replace("1111", "22", 1)
        s = s.replace("222", "1", 1)

    if max1 < s.count("1"):
        max1 = s.count("1")
        print("Наибольшее количество единиц =", max1, "самая короткая строка содержит", n, "единиц")
        if max1 == 4:
            break
    n += 1

# https://inf-ege.sdamgia.ru/problem?id=8664
n = 8**2020 + 4**2017 + 26 - 1
n = bin(n)[2:]
print(n.count("1"))

# Двоичная bin (binary), восьмеричная oct (octal), шестнадцатеричная hex (hexademical)

# https://inf-ege.sdamgia.ru/problem?id=13743
a = 49**10 + 7**30 - 49
a_7 = ""
while a != 0:
    a_7 += str(a % 7)
    a //= 7
a_7 = a_7[::-1]
print(a_7.count("6"))

# https://inf-ege.sdamgia.ru/problem?id=47218
for x in range(15):
    a = 1*15**4 + 2*15**3 + 3*15**2 + x*15**1 + 5*15**0
    b = 1*15**4 + x*15**3 + 2*15**2 + 3*15**1 + 3*15**0
    c = a + b
    if c % 14 == 0:
        print(x, c // 14)
        

# https://inf-ege.sdamgia.ru/problem?id=48380
search = True
a = 1
while search:
    for x in range(12):
        m = 4*12**4 + 9*12**3 + x*12**2 + 2*12**1 + 6*12**0
        n = 4*12**4 + 9*12**3 + x*12**2 + 7*12**1 + 0*12**0
        if (m + a) % n == 0:
            print("М + А кратно N при х =", x, "и А =", a)
            search = False
            break
    a += 1

# https://inf-ege.sdamgia.ru/problem?id=58481
search = True
p = 2
while search:
    for x in range(p):
        for y in range(p):
            a = 1*p**1 + 2*p**0
            b = 3*p**1 + 4*p**0
            c = (x*p**1 + y*p**0)**2
            if (a * b) == c:
                print(p, x, y)
                search = False
                break
    p += 1

# https://inf-ege.sdamgia.ru/problem?id=48395
for x in range(12):
    a = 2*18**3 + 8*18**2 + x*18**1 + 2*18**0
    b = 9*12**3 + 3*12**2 + x*12**1 + 5*12**0
    c = a + b 
    if c % 133 == 0:
        print(x, c // 133)

# В некоторых задачах буквы в больших системах счисления надо заменять на числа
# A = 10, B = 11, C = 12, D = 13, E = 14, F = 15
        
# https://inf-ege.sdamgia.ru/problem?id=48393
for x in range(8):
    for y in range (8):
        a = y*11**4 + 0*11**3 + 4*11**2+x*11**1 + 5*11**0
        b = 2*8**4 + 5*8**3 + 3*8**2 + x*8**1 + y*8**0
        c = a + b
        if c % 117 == 0:
            print (c // 117)

# https://inf-ege.sdamgia.ru/problem?id=8094
def f(n):
    n_2 = bin(n)[2:]
    
    sum_n_2 = n_2.count("1")
    n_2 += str(sum_n_2 % 2)

    sum_n_2 = n_2.count("1")
    n_2 += str(sum_n_2 % 2)

    r = int(n_2, 2)
    return r

n = 1
while True:
    if f(n) > 43:
        print("Предположительный ответ при n =", n, ", r =", f(n))
        break
    n += 1

# print("11111000" + str(5 % 2))

# https://inf-ege.sdamgia.ru/problem?id=9298
def f(n):
    s = str(n)
    sum12 = int(s[0]) + int(s[1])
    sum23 = int(s[1]) + int(s[2])
    sums = [sum12, sum23]
    sums.sort()
    sums = sums[::-1]
    r = "".join([str(a) for a in sums])
    return r

for n in range(100, 1000):
    if f(n) == "1715":
        print(n)