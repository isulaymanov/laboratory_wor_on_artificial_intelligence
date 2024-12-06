import numpy as np

# 21. Создать 8x8 матрицу и заполнить её в шахматном порядке, используя функцию tile
Z = np.tile(np.array([[0, 1], [1, 0]]), (4, 4))
print("Task 21:\n", Z)

# 22. Перемножить матрицы 5x3 и 3x2
Z = np.dot(np.ones((5, 3)), np.ones((3, 2)))
print("\nTask 22:\n", Z)

# 23. Дан массив, поменять знак у элементов, значения которых между 3 и 8
Z = np.arange(11)
Z[(3 < Z) & (Z <= 8)] *= -1
print("\nTask 23:\n", Z)

# 24. Создать 5x5 матрицу со значениями в строках от 0 до 4
Z = np.zeros((5, 5))
Z += np.arange(5)
print("\nTask 24:\n", Z)

# 25. Есть генератор, сделать с его помощью массив
def generate():
    for x in range(10):
        yield x

Z = np.fromiter(generate(), dtype=float, count=-1)
print("\nTask 25:\n", Z)

# 26. Создать вектор размера 10 со значениями от 0 до 1, не включая ни то, ни другое
Z = np.linspace(0, 1, 12)[1:-1]
print("\nTask 26:\n", Z)

# 27. Отсортировать вектор
Z = np.random.random(10)
Z.sort()
print("\nTask 27:\n", Z)

# 28. Проверить, одинаковы ли 2 массива
A = np.random.randint(0, 5, 5)
B = np.random.randint(0, 5, 5)
equal = np.allclose(A, B)
print("\nTask 28:")
print("A:", A)
print("B:", B)
print("Are equal:", equal)
