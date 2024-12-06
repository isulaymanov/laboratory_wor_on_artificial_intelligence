import numpy as np

# 1. Импортировать NumPy под именем np
# (уже сделано выше)

# 2. Напечатать версию и конфигурацию
print("Task 2:")
print(np.__version__)
np.show_config()

# 3. Создать вектор (одномерный массив) размера 10, заполненный нулями
Z = np.zeros(10)
print("\nTask 3:\n", Z)

# 4. Создать вектор размера 10, заполненный единицами
Z = np.ones(10)
print("\nTask 4:\n", Z)

# 5. Создать вектор размера 10, заполненный числом 2.5
Z = np.full(10, 2.5)
print("\nTask 5:\n", Z)

# 6. Получить документацию о функции numpy.add из командной строки
# В командной строке: python3 -c "import numpy; numpy.info(numpy.add)"

# 7. Создать вектор размера 10, но пятый элемент равен 1
Z = np.zeros(10)
Z[4] = 1
print("\nTask 7:\n", Z)

# 8. Создать вектор со значениями от 10 до 49
Z = np.arange(10, 50)
print("\nTask 8:\n", Z)

# 9. Развернуть вектор (первый элемент становится последним)
Z = np.arange(50)[::-1]
print("\nTask 9:\n", Z)

# 10. Создать матрицу 3x3 со значениями от 0 до 8
Z = np.arange(9).reshape(3, 3)
print("\nTask 10:\n", Z)

# 11. Найти индексы ненулевых элементов в [1,2,0,0,4,0]
nz = np.nonzero([1, 2, 0, 0, 4, 0])
print("\nTask 11:\n", nz)

# 12. Создать 3x3 единичную матрицу
Z = np.eye(3)
print("\nTask 12:\n", Z)

# 13. Создать массив 3x3x3 со случайными значениями
Z = np.random.random((3, 3, 3))
print("\nTask 13:\n", Z)

# 14. Создать массив 10x10 со случайными значениями, найти минимум и максимум
Z = np.random.random((10, 10))
Zmin, Zmax = Z.min(), Z.max()
print("\nTask 14:\nMin:", Zmin, "Max:", Zmax)

# 15. Создать случайный вектор размера 30 и найти среднее значение
Z = np.random.random(30)
m = Z.mean()
print("\nTask 15:\n", m)

# 16. Создать матрицу с 0 внутри, и 1 на границах
Z = np.ones((10, 10))
Z[1:-1, 1:-1] = 0
print("\nTask 16:\n", Z)

# 17. Выяснить результат следующих выражений
print("\nTask 17:")
print(0 * np.nan)  # nan
print(np.nan == np.nan)  # False
print(np.inf > np.nan)  # False
print(np.nan - np.nan)  # nan
print(0.3 == 3 * 0.1)  # False

# 18. Создать 5x5 матрицу с 1, 2, 3, 4 под диагональю
Z = np.diag(np.arange(1, 5), k=-1)
print("\nTask 18:\n", Z)

# 19. Создать 8x8 матрицу в шахматном порядке
Z = np.zeros((8, 8), dtype=int)
Z[1::2, ::2] = 1
Z[::2, 1::2] = 1
print("\nTask 19:\n", Z)

# 20. Дан массив размерности (6,7,8). Какой индекс (x,y,z) сотого элемента?
print("\nTask 20:")
print(np.unravel_index(100, (6, 7, 8)))
