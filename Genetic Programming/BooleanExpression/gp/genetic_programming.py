import random
from gp.expression import random_expression, evaluate, mutate, crossover, expr_to_str
from copy import deepcopy


def fitness(expr, dataset):
    correct = 0
    for sample, output in dataset:
        pred = evaluate(expr, sample)
        if pred == output:
            correct += 1
    return correct / len(dataset)

def run_gp(dataset, pop_size=50, generations=50):
    population = [random_expression() for _ in range(pop_size)]
    fitness_progress = []
    best_individuals = []

    for gen in range(generations):
        scored_pop = [(ind, fitness(ind, dataset)) for ind in population]
        scored_pop.sort(key=lambda x: x[1], reverse=True)

        fitness_progress.append(scored_pop[0][1])
        best_individuals.append(deepcopy(scored_pop[0][0]))

        new_population = [scored_pop[0][0], scored_pop[1][0]]

        while len(new_population) < pop_size:
            t1 = random.choice(scored_pop[:10])[0]
            t2 = random.choice(scored_pop[:10])[0]
            child = crossover(t1, t2)
            child = mutate(child)
            new_population.append(child)

        population = new_population

    final_best = scored_pop[0][0]
    print("\nBest Expression:")
    print(expr_to_str(final_best))
    print(f"Fitness: {scored_pop[0][1]}")

    return best_individuals, fitness_progress, final_best