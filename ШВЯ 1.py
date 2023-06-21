A = [5, 14, -21, 7, 0, -35, 42, -28, 3, -7]
sum_negative_multiple_7 = 0
count_negative_multiple_7 = 0

for i in A:
    if i < 0 and i % 7 == 0:
        sum_negative_multiple_7 += i
        count_negative_multiple_7 += 1

print(f"Сумма отрицательных элементов кратных 7: {sum_negative_multiple_7}")
print(f"Количество отрицательных элементов кратных 7: {count_negative_multiple_7}")