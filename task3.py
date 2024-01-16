# Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
# Достаточно вернуть один допустимый вариант. *Верните все возможные варианты комплектации рюкзака.

def fill_bag(items, max_weight):
    def recursive_fill(bag, my_items, weight):
        if weight == 0 or len(my_items) == 0:
            return bag

        next_item = my_items[0]
        next_item_weight = items[next_item]

        if next_item_weight <= weight:
            updated_bag = bag.copy()
            updated_bag[next_item] = next_item_weight
            updated_weight = weight - next_item_weight

            result = recursive_fill(updated_bag, my_items[1:], updated_weight)

            if result is not None:
                return result

        return recursive_fill(bag, my_items[1:], weight)

    bag = {}
    my_items = list(items.keys())

    return recursive_fill(bag, my_items, weight)



items = {"Палатка": 2000, "Спальник": 1000, "Кружка": 200, "Котелок": 500, "Тент": 3000}
weight = 3500

result = fill_bag(items, weight)
print(result)

