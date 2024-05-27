# Дані про їжу
items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

def greedy_algorithm(items, budget):
    sorted_items = sorted(items.items(), key=lambda x: x[1]['calories'] / x[1]['cost'], reverse=True)
    total_cost = 0
    total_calories = 0
    chosen_items = []

    for item, details in sorted_items:
        if total_cost + details['cost'] <= budget:
            chosen_items.append(item)
            total_cost += details['cost']
            total_calories += details['calories']

    return chosen_items, total_cost, total_calories

def dynamic_programming(items, budget):
    item_list = list(items.items())
    n = len(item_list)
    dp = [[0 for _ in range(budget + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        item, details = item_list[i - 1]
        cost = details['cost']
        calories = details['calories']

        for w in range(budget + 1):
            if cost <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - cost] + calories)
            else:
                dp[i][w] = dp[i - 1][w]

    w = budget
    chosen_items = []
    total_cost = 0
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            item, details = item_list[i - 1]
            chosen_items.append(item)
            total_cost += details['cost']
            w -= details['cost']

    chosen_items.reverse()
    total_calories = dp[n][budget]
    return chosen_items, total_cost, total_calories

budget = 100

greedy_items, greedy_total_cost, greedy_total_calories = greedy_algorithm(items, budget)
print(f"Жадібний алгоритм вибрав наступні страви:")
for item in greedy_items:
    print(f"- {item} (Вартість: {items[item]['cost']}, Калорійність: {items[item]['calories']})")
print(f"Загальна вартість: {greedy_total_cost}, Загальна калорійність: {greedy_total_calories}\n")

dp_items, dp_total_cost, dp_total_calories = dynamic_programming(items, budget)
print(f"Динамічне програмування вибрало наступні страви:")
for item in dp_items:
    print(f"- {item} (Вартість: {items[item]['cost']}, Калорійність: {items[item]['calories']})")
print(f"Загальна вартість: {dp_total_cost}, Загальна калорійність: {dp_total_calories}")
