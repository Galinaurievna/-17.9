array = list(map(int, input("Введите числа через пробел:").split()))
print(array)
# сортируем введенную последовательность чисел
for i in range(1, len(array)):
    x = array[i]
    idx = i
    while idx > 0 and array[idx-1] > x:
        array[idx] = array[idx-1]
        idx -= 1
    array[idx] = x
print(array)

element = int(input("Введите число в рамках последовательности"))
# проверяем корректность введенного числа
while element:
    if element not in range(min(array)+1, max(array)):
        print("Введено некорректное число")
        element = int(input("Введите число в рамках последовательности"))
    else:
        break
array.append(element) # добавляем введенное число в последовательность
# снова сортируем последовательность чисел
for i in range(1, len(array)):
    x = array[i]
    idx = i
    while idx > 0 and array[idx-1] > x:
        array[idx] = array[idx-1]
        idx -= 1
    array[idx] = x
print(array)
# Устанавливается номер позиции элемента, который меньше введенного пользователем числа, а следующий за ним больше или равен этому числу.
def binary_search(array, element, left, right):
    if left > right:  # если левая граница превысила правую,
        return False  # значит элемент отсутствует
    middle = (right + left) // 2  # находимо середину
    if array[middle] == element:  # если элемент в середине,
        return middle  # возвращаем этот индекс
    elif element < array[middle]:  # если элемент меньше элемента в середине
        # рекурсивно ищем в левой половине
        return binary_search(array, element, left, middle - 1)
    else:  # иначе в правой
        return binary_search(array, element, middle + 1, right)
a = (binary_search(array, element, 0, len(array)-1))
print("Номер позиции элемента, который меньше введенного пользователем числа:")
print(a-1)
print("Номер позиции элемента, который больше или равен этому числу:")
print(a+1)