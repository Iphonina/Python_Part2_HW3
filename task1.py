# Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов.

def find_dupl(lst):
    uniq_elements = set()
    duplicates = []

    for element in lst:
        if element not in uniq_elements:
            uniq_elements.add(element)
        else:
            duplicates.append(element)

    return duplicates


numbers = [1, 7, 1, 3, 4, 4, 8, 5, 5]

duplicates = find_dupl(numbers)
print(duplicates)
