import random

# Ideal traits (girlfriend preference)
IDEAL = {
    "looks": 8,
    "humor": 9,
    "money": 7,
    "kindness": 8
}

TRAITS = list(IDEAL.keys())

# Generate random boyfriend
def create_boyfriend():
    return {trait: random.randint(1, 10) for trait in TRAITS}

# Fitness function
def fitness(bf):
    diff = sum(abs(bf[t] - IDEAL[t]) for t in TRAITS)
    return 1 / (1 + diff)

# Selection (top 50%)
def selection(population):
    return sorted(population, key=fitness, reverse=True)[:len(population)//2]

# Crossover
def crossover(p1, p2):
    child = {}
    for trait in TRAITS:
        # randomly pick from either parent
        child[trait] = random.choice([p1[trait], p2[trait]])
    return child

# Mutation
def mutate(bf, rate=0.1):
    for trait in TRAITS:
        if random.random() < rate:
            bf[trait] = random.randint(1, 10)
    return bf

# Main GA
def genetic_algorithm():
    population = [create_boyfriend() for _ in range(6)]
    
    for gen in range(5):
        print(f"\nGeneration {gen}")
        
        for bf in population:
            print(bf, "Fitness:", round(fitness(bf), 3))
        
        # Selection
        selected = selection(population)
        
        # New generation
        new_population = selected.copy()
        
        while len(new_population) < 6:
            p1, p2 = random.sample(selected, 2)
            child = crossover(p1, p2)
            child = mutate(child)
            new_population.append(child)
        
        population = new_population

genetic_algorithm()

'''Dry Run (Dictionary Style)
Initial Population
{'looks': 5, 'humor': 7, 'money': 6, 'kindness': 6}
{'looks': 9, 'humor': 9, 'money': 8, 'kindness': 7}
{'looks': 6, 'humor': 8, 'money': 5, 'kindness': 7}
...
Fitness Calculation Example

For:

bf = {'looks': 5, 'humor': 7, 'money': 6, 'kindness': 6}

Compare with:

IDEAL = {'looks': 8, 'humor': 9, 'money': 7, 'kindness': 8}

Compute:

diff = |5-8| + |7-9| + |6-7| + |6-8|
     = 3 + 2 + 1 + 2 = 8

fitness = 1 / (1 + 8) = 0.111
Crossover Example
Parent1 = {'looks': 9, 'humor': 9, 'money': 8, 'kindness': 7}
Parent2 = {'looks': 6, 'humor': 8, 'money': 5, 'kindness': 7}

Child (random mixing):

Child = {
    'looks': 9,      # from Parent1
    'humor': 8,      # from Parent2
    'money': 8,      # from Parent1
    'kindness': 7    # from Parent2
}
Mutation Example

Before:

{'looks': 9, 'humor': 8, 'money': 8, 'kindness': 7}

After mutation:

{'looks': 9, 'humor': 10, 'money': 8, 'kindness': 7}

population.sort(key=lambda x: fitness(x), reverse=True)
return population[:len(population)//2]
🧠 What This Is Doing (Big Picture)

This is the selection step of the genetic algorithm:

👉 “Keep the best half, discard the weaker half.”

🧩 Line 1: Sorting by Fitness
population.sort(key=lambda x: fitness(x), reverse=True)
Step-by-step:
1. population.sort(...)
Sorts the list in-place
After this, original order is gone
2. key=lambda x: fitness(x)

This is the tricky part.

👉 It means:

“Sort each boyfriend based on their fitness score.”

x = one boyfriend (a dictionary)
fitness(x) = how good that boyfriend is

So internally Python does something like:

fitness(bf1), fitness(bf2), fitness(bf3), ...
3. reverse=True
Normally sorting is ascending (small → big)
But we want best first

So:

reverse=True  → highest fitness comes first
✅ Result After Sorting

Before:

[
 bfA (fitness 0.1),
 bfB (fitness 0.3),
 bfC (fitness 0.2)
]

After sorting:

[
 bfB (0.3),   # best
 bfC (0.2),
 bfA (0.1)    # worst
]
🧩 Line 2: Taking Top Half
return population[:len(population)//2]
Step-by-step:
1. len(population)//2
Suppose population size = 6
Then:
6 // 2 = 3
2. population[:3]

This means:
👉 “Take first 3 elements”

Since list is already sorted:

Top 3 = best 3 boyfriends
✅ Final Result
[
 best_bf,
 second_best_bf,
 third_best_bf
]

def mutate(bf, rate=0.1):
    for trait in bf:
        if random.random() < rate:
            bf[trait] = random.randint(1, 10)
    return bf
🔍 Now Let’s Understand Mutation Step-by-Step
Step 1: Loop Over Traits
for trait in bf:

If:

bf = {"looks": 6, "humor": 8, "money": 5, "kindness": 7}

Loop goes like:

"looks" → "humor" → "money" → "kindness"
Step 2: Random Chance Check
if random.random() < rate:
random.random() gives a number between 0 and 1
rate = 0.1 → 10% chance

👉 So each trait has 10% chance to mutate

Example Random Values
Trait	Random Value	Mutate?
looks	0.05	✅ Yes
humor	0.7	❌ No
money	0.02	✅ Yes
kindness	0.5	❌ No
Step 3: Apply Mutation
bf[trait] = random.randint(1, 10)

👉 Replace old value with a new random value

Example

Before:

{"looks": 6, "humor": 8, "money": 5, "kindness": 7}

After mutation:

{"looks": 9, "humor": 8, "money": 2, "kindness": 7}

(looks & money changed)

🎯 Why Mutation Exists

Without mutation:

Population becomes too similar
Algorithm gets stuck (local optimum)

Mutation adds:

Randomness
Exploration
New traits
🧪 Mini Dry Run
bf = {"looks": 8, "humor": 9, "money": 7, "kindness": 8}
rate = 0.1

Random outcomes:

looks → 0.3  → no change
humor → 0.01 → mutate → becomes 10
money → 0.8  → no change
kindness → 0.05 → mutate → becomes 6

Final:

{"looks": 8, "humor": 10, "money": 7, "kindness": 6}

The Code
def genetic_algorithm():
    population = [create_boyfriend() for _ in range(6)]
    
    for gen in range(5):
        print(f"\nGeneration {gen}")
        
        for bf in population:
            print(bf, "Fitness:", round(fitness(bf), 3))
        
        # Selection
        selected = selection(population)
        
        # New generation
        new_population = selected.copy()
🧠 Step 1: Initial Population
population = [create_boyfriend() for _ in range(6)]
What this means:
Create 6 random boyfriends
_ just means “we don’t care about the loop variable”
Example:
population = [
 {'looks': 5, 'humor': 7, 'money': 6, 'kindness': 6},
 {'looks': 9, 'humor': 9, 'money': 8, 'kindness': 7},
 {'looks': 6, 'humor': 8, 'money': 5, 'kindness': 7},
 {'looks': 3, 'humor': 4, 'money': 6, 'kindness': 5},
 {'looks': 7, 'humor': 7, 'money': 6, 'kindness': 8},
 {'looks': 8, 'humor': 6, 'money': 7, 'kindness': 6}
]

👉 This is Generation 0

🔁 Step 2: Loop Over Generations
for gen in range(5):

👉 Run the evolution 5 times

So:

gen = 0 → first generation
gen = 1 → next generation
...
gen = 4 → last generation
🖨️ Step 3: Print Current Population
print(f"\nGeneration {gen}")

for bf in population:
    print(bf, "Fitness:", round(fitness(bf), 3))
What happens:

For each boyfriend:

Show traits
Compute fitness
Print result
Example Output
Generation 0
{'looks': 5, 'humor': 7, 'money': 6, 'kindness': 6} Fitness: 0.111
{'looks': 9, 'humor': 9, 'money': 8, 'kindness': 7} Fitness: 0.25
...

👉 This lets you observe evolution happening

🧬 Step 4: Selection
selected = selection(population)
What happens:
Population is sorted by fitness
Top 50% are kept
Example:

Before:

6 boyfriends

After:

3 best boyfriends
selected = [
 best_bf,
 second_best_bf,
 third_best_bf
]

👉 Weak candidates are removed

🧪 Step 5: Start New Generation
new_population = selected.copy()
This is subtle but important:

👉 We directly carry forward the best candidates

This is called:

⭐ Elitism (important GA concept)

Meaning:

“Don't lose the best solutions”

Example:
selected = [
 A, B, C
]

After copy:

new_population = [
 A, B, C
]
🤔 Why Copy?

If we didn't do this:

We might lose good solutions during crossover/mutation
Evolution could go backward

So we ensure:

👉 Best candidates survive unchanged

Mathematical Intuition behind Optimization

Each generation:
Average fitness increases
Difference from IDEAL decreases

This is called: Convergence'''