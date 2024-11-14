import random


def objective_function(x):
    return sum(x_i**2 for x_i in x)


num_particles = 30
dim = 2
max_iter = 100
w = 0.5
c1 = 1.5
c2 = 1.5
particles = [{'position': [random.uniform(-10, 10) for _ in range(dim)],
              'velocity': [random.uniform(-1, 1) for _ in range(dim)],
              'best_position': None,
              'best_value': float('inf')} for _ in range(num_particles)]
global_best_position = None
global_best_value = float('inf')
for iteration in range(max_iter):
    for particle in particles:
        current_value = objective_function(particle['position'])
        if current_value < particle['best_value']:
            particle['best_value'] = current_value
            particle['best_position'] = particle['position']
        if current_value < global_best_value:
            global_best_value = current_value
            global_best_position = particle['position']
    for particle in particles:
        for i in range(dim):
            r1 = random.random()
            r2 = random.random()
            particle['velocity'][i] = (w * particle['velocity'][i] +
                                       c1 * r1 * (particle['best_position'][i] - particle['position'][i]) +
                                       c2 * r2 * (global_best_position[i] - particle['position'][i]))
            particle['position'][i] = particle['position'][i] + \
                particle['velocity'][i]
    print(f"Iteration {iteration +
                                 1}/{max_iter}, Global Best Value: {global_best_value}")

    print("Optimal Solution:", global_best_position)
    print("Optimal Value:", global_best_value)
    
