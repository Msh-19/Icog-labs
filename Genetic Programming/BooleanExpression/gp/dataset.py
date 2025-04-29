from itertools import product

def create_dataset():
    variables = ['A', 'B', 'C']

    def target_function(sample):
        A, B, C = sample['A'], sample['B'], sample['C']
        return (A and not B) or C

    dataset = []
    for values in product([0, 1], repeat=len(variables)):
        sample = dict(zip(variables, values))
        output = target_function(sample)
        dataset.append((sample, output))
    
    return dataset