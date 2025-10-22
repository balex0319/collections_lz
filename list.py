N = int(input('Введите количество элементов в  ряде Фибоначчи: ')) 
a=0 
b=1 
c=0 
l = list = [] 
for i in range (0, N): 
    l.append(a) 
    a, b = b, a + b 
print("Ряд Фибоначчи:" , l)
for i in range(0,len(l),2): 
    l[i] = l[i]*2
for i in range(1,len(l),2):
    l[i] = l[i]**2
print("Измененный ряд Фибоначчи:" , l)
print("Минимальный элемент ряда:" , min(l))
print("Максимальный элемент ряда:" , max(l))
print("Длина измененного ряда:" , len(l))
med = len(l)//2
print("Медианное значание ряда:" , med)
for i in range(0,len(l)): 
    if l[i] > med:
        c += 1
print("Количество элементов, большее медианного значения:" , c) 