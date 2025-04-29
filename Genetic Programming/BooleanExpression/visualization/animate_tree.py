import matplotlib.pyplot as plt
import matplotlib.animation as animation
import networkx as nx

def build_tree(expr, graph=None, parent=None, name_generator=None):
    if graph is None:
        graph = nx.DiGraph()
    if name_generator is None:
        name_generator = iter(range(10000))

    current = next(name_generator)
    label = expr if isinstance(expr, str) else expr[0]
    graph.add_node(current, label=label)
    if parent is not None:
        graph.add_edge(parent, current)

    if not isinstance(expr, str):
        if expr[0] == 'NOT':
            build_tree(expr[1], graph, current, name_generator)
        else:
            build_tree(expr[1], graph, current, name_generator)
            build_tree(expr[2], graph, current, name_generator)

    return graph

def animate_trees(best_individuals):
    fig, ax = plt.subplots(figsize=(10, 6))

    def update(frame):
        ax.clear()
        G = build_tree(best_individuals[frame])
        pos = nx.nx_pydot.graphviz_layout(G, prog="dot")
        labels = nx.get_node_attributes(G, 'label')
        nx.draw(G, pos, with_labels=True, labels=labels, arrows=True,
                node_size=2000, node_color='skyblue', font_size=10, ax=ax)
        ax.set_title(f'Generation {frame+1}')

    ani = animation.FuncAnimation(fig, update, frames=len(best_individuals), interval=300)
    plt.show()
