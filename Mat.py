import random
import matplotlib.pyplot as plt

IDEAL = {
    "looks": 8,
    "humor": 9,
    "money": 7,
    "kindness": 8
}

TRAITS = list(IDEAL.keys())

def create_boyfriend():
    return {trait: random.randint(1, 10) for trait in TRAITS}

def fitness(bf):
    diff = sum(abs(bf[t] - IDEAL[t]) for t in TRAITS)
    return 1 / (1 + diff)

def selection(population):
    return sorted(population, key=fitness, reverse=True)[:len(population)//2]

def crossover(p1, p2):
    return {t: random.choice([p1[t], p2[t]]) for t in TRAITS}

def mutate(bf, rate=0.1):
    for t in TRAITS:
        if random.random() < rate:
            bf[t] = random.randint(1, 10)
    return bf

def genetic_algorithm():
    population = [create_boyfriend() for _ in range(10)]
    best_fitness_history = []

    for gen in range(20):
        # Track best fitness
        best = max(population, key=fitness)
        best_fitness_history.append(fitness(best))

        print(f"Gen {gen} Best:", best, "Fitness:", round(fitness(best), 3))

        # Selection
        selected = selection(population)

        # New generation
        new_population = selected.copy()

        while len(new_population) < 10:
            p1, p2 = random.sample(selected, 2)
            child = crossover(p1, p2)
            child = mutate(child)
            new_population.append(child)

        population = new_population

    return best_fitness_history

# Run GA
history = genetic_algorithm()

# Plot
plt.plot(history, marker='o')
plt.title("Genetic Algorithm Optimization")
plt.xlabel("Generation")
plt.ylabel("Best Fitness")
plt.grid()
plt.show()