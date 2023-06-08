def fibo(a): #массив с числами Фибоначчи
    mas0 = ['1', '1']
    for _ in range(a-2):
        mas0.append(str(int(mas0[-1]) + int(mas0[-2])))
    return mas0

masf = fibo(500)
s = ''.join(masf)
def brute_force(s): #наивный алгоритм
    max_k = 0
    max_i = 0
    def vspom(a, s):  # вспомогательная функция для перебора
        k = 0
        for i in range(len(s) - 1):
            if s[i] + s[i + 1] == str(a):
                k += 1
        return k
    for i in range(10, 100):
        n =vspom(str(i), s)
        if n > max_k:
            max_k = n
            max_i = i
        print(i, n)
    return max_i, max_k
def hash(s): #алгоритм Рабина-Карпа
    max_k = 0
    for i in range(10, 100):
        mas0 = []
        k = 0
        for j in range(len(s)-1):
            if int(s[j]+s[j+1]) == i: #проверка хэша и заполнение массива
                mas0.append(s[j]+s[j+1])
        for j in mas0:
            if j == str(i): #перебор значений в массиве
                k += 1
        if k > max_k:
            max_k = k
            max_i = i
        print(i, k)
    return max_i, max_k
def boyer_mur(s): #алгоритм Бойера-Мура
    max_k = 0
    for i in range(10, 100):
        s1 = s
        k = 0
        while len(s1) > 1:
            if i % 10 == int(s1[1]):
                if i // 10 == int(s1[0]):
                    k += 1
                if i // 10 == int(s1[1]):
                    s1 = s1[1:]
                else:
                    s1 = s1[2:]
            elif i // 10 == int(s1[1]):
                s1 = s1[1:]
            else:
                s1 = s1[2:]
        if k > max_k:
            max_k = k
            max_i = i
        print(i, k)
    return max_i, max_k

#Алгоритм Кнута-Морриса-Пратта
#Создаем массив пи
def CreatePiList(arr):
    pi = [0]*len(arr)
    pi[0] = 0
    j = 0
    i = 1
    while i < len(arr):
        if arr[i] == arr[j]:
            pi[i] = j+1
            i += 1
            j += 1
        elif j == 0:
            pi[i] = 0
            i += 1
        else:
            j = pi[j-1]
    return pi
#Движения с индексами
def KMPsearch(s,txt):
    pi = CreatePiList(s)
    k=0 #индекс в образе
    l=0 #индекс в тексте
    count = 0
    while l < len(txt):
        if s[k] == txt[l]:
            k += 1
            l += 1
            if k == len(s):
                count += 1
                k=0
        elif s[k] != txt[l] and k != 0:
            k = pi[k-1]
        elif s[k] != txt[l] and k == 0:
            l+=1
    return count

out = hash(s)
print("Максимальное число совпадений с числом {0}: {1}".format(out[0], out[1]) )
print(KMPsearch(str(out[0]), s))