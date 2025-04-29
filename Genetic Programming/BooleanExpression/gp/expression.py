import random
import copy

operators = ['AND', 'OR', 'NOT']
operands = ['A', 'B', 'C', '0', '1']

def random_expression(depth=0, max_depth=3):
    if depth > max_depth or (depth > 0 and random.random() < 0.3):
        return random.choice(operands)
    op = random.choice(operators)
    if op == 'NOT':
        return (op, random_expression(depth+1, max_depth))
    else:
        return (op, random_expression(depth+1, max_depth), random_expression(depth+1, max_depth))

def evaluate(expr, sample):
    if isinstance(expr, str):
        if expr in sample:
            return sample[expr]
        else:
            return int(expr)
    op = expr[0]
    if op == 'NOT':
        return not evaluate(expr[1], sample)
    elif op == 'AND':
        return evaluate(expr[1], sample) and evaluate(expr[2], sample)
    elif op == 'OR':
        return evaluate(expr[1], sample) or evaluate(expr[2], sample)

def mutate(expr, prob=0.1):
    if isinstance(expr, str):
        if random.random() < prob:
            return random_expression()
        else:
            return expr
    else:
        if random.random() < prob:
            return random_expression()
        else:
            op = expr[0]
            if op == 'NOT':
                return (op, mutate(expr[1], prob))
            else:
                return (op, mutate(expr[1], prob), mutate(expr[2], prob))

def crossover(expr1, expr2, prob=0.7):
    if random.random() > prob:
        return copy.deepcopy(expr1)
    if isinstance(expr1, str) or isinstance(expr2, str):
        return copy.deepcopy(expr2)
    if expr1[0] != expr2[0]:
        return copy.deepcopy(expr2)
    op = expr1[0]
    if op == 'NOT':
        return (op, crossover(expr1[1], expr2[1], prob))
    else:
        return (op, crossover(expr1[1], expr2[1], prob), crossover(expr1[2], expr2[2], prob))

def expr_to_str(expr):
    if isinstance(expr, str):
        return expr
    op = expr[0]
    if op == 'NOT':
        return f"NOT({expr_to_str(expr[1])})"
    else:
        return f"({expr_to_str(expr[1])} {op} {expr_to_str(expr[2])})"