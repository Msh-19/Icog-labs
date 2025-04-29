from gp.dataset import create_dataset
from gp.genetic_programming import run_gp
from visualization.plot_fitness import plot_fitness
from visualization.animate_tree import animate_trees

# Create dataset
dataset = create_dataset()

# Run GP
best_individuals, fitness_progress, best_expr = run_gp(dataset)

# Plot
plot_fitness(fitness_progress)

# Animate
animate_trees(best_individuals)
