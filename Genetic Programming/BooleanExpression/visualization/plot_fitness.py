import matplotlib.pyplot as plt

def plot_fitness(fitness_progress):
    plt.plot(fitness_progress)
    plt.title('Fitness over Generations')
    plt.xlabel('Generation')
    plt.ylabel('Fitness')
    plt.grid()
    plt.show()