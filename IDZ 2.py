A = [-5.4, 14.1, -21.7, 7.3, 0.6, -35.2, 42.8, -28.9, 3.2, -7.1]

# Номер максимального по модулю элемента списка
max_abs_index = 0
for i in range(len(A)):
    if abs(A[i]) > abs(A[max_abs_index]):
        max_abs_index = i

print(f"Номер максимального по модулю элемента списка: {max_abs_index}")

# Сумма элементов списка, расположенных после первого положительного элемента
sum_after_positive = 0
positive_found = False
for i in A:
    if i > 0:
        positive_found = True
    elif positive_found:
        sum_after_positive += i

print(f"Сумма элементов списка после первого положительного элемента: {sum_after_positive}")