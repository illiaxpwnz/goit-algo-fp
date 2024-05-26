import random
import matplotlib.pyplot as plt

def simulate_dice_rolls(num_rolls):
    results = [0] * 13 

    for _ in range(num_rolls):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        result = dice1 + dice2
        results[result] += 1

    return results

def calculate_probabilities(results, num_rolls):
    probabilities = {}
    for sum_value in range(2, 13):
        probabilities[sum_value] = results[sum_value] / num_rolls * 100
    return probabilities

def plot_probabilities(probabilities):
    sums = list(probabilities.keys())
    probs = list(probabilities.values())

    plt.bar(sums, probs, color='skyblue', edgecolor='black')
    plt.xlabel('Сума')
    plt.ylabel('Ймовірність (%)')
    plt.title('Ймовірності сум при киданні двох кубиків (Метод Монте-Карло)')
    plt.xticks(range(2, 13))
    plt.grid(axis='y')
    plt.show()

def main():
    num_rolls = 1000000  # Велика кількість кидків
    results = simulate_dice_rolls(num_rolls)
    probabilities = calculate_probabilities(results, num_rolls)

    print("Сума\tІмовірність (%)")
    for sum_value in range(2, 13):
        print(f"{sum_value}\t{probabilities[sum_value]:.2f}%")

    plot_probabilities(probabilities)

    # Аналітичні ймовірності для порівняння
    analytical_probabilities = {
        2: 1/36 * 100,
        3: 2/36 * 100,
        4: 3/36 * 100,
        5: 4/36 * 100,
        6: 5/36 * 100,
        7: 6/36 * 100,
        8: 5/36 * 100,
        9: 4/36 * 100,
        10: 3/36 * 100,
        11: 2/36 * 100,
        12: 1/36 * 100
    }

    print("\nАналітичні ймовірності:")
    print("Сума\tІмовірність (%)")
    for sum_value in range(2, 13):
        print(f"{sum_value}\t{analytical_probabilities[sum_value]:.2f}%")

if __name__ == "__main__":
    main()
