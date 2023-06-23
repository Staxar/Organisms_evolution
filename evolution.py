import random

# Determinate organisms structure
class Organism:
    def __init__(self, speed, strength, agility):
        self.speed = speed
        self.strength = strength
        self.agility = agility

    def fitness(self):
        return self.speed + self.strength + self.agility #score

# Init population
def create_population(population_size):
    population = []
    for _ in range(population_size):
        speed = random.randint(1, 10)
        strength = random.randint(1,10)
        agility = random.randint(1, 8)
        organism = Organism(speed, strength, agility)
        population.append(organism)
    return population

# Best organisms selection
def selection(population, num_parents):
    population = sorted(population, key=lambda x: x.fitness(), reverse=True)
    parents = population[:num_parents]
    return parents

# Crossing parents
def crossover(parents, population_size):
    offspring = []
    for _ in range(population_size):
        parent1 = random.choice(parents)
        parent2 = random.choice(parents)
        speed = random.choice([parent1.speed, parent2.speed])
        strength = random.choice([parent1.strength, parent2.strength])
        agility = random.choice([parent1.agility, parent2.agility])
        organism = Organism(speed, strength, agility)
        offspring.append(organism)
    return offspring

# Mutation
def mutation(population, mutation_rate):
    for organism in population:
        if random.random() < mutation_rate:
            organism.speed = random.randint(1, 10)
            organism.strength = random.randint(1, 10)
            organism.agility = random.randint(1, 10)
    return population

population_size = 1000
num_generations = 10
num_parents = 10
mutation_rate = 0.1

population = create_population(population_size)

for generation in range(num_generations):
    parents = selection(population, num_parents)
    offspring = crossover(parents, population_size - num_parents)
    population = parents + offspring
    population = mutation(population, mutation_rate)

    # Wyświetlanie informacji o każdej generacji
    best_organism = max(population, key=lambda x: x.fitness())
    print(f"Generation: {generation+1}  Best Fitness: {best_organism.fitness()}")