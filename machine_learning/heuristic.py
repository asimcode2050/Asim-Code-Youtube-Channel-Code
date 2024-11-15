import random


def generate_code(function_name, parameters):
    code = f"def {function_name}({', '.join(parameters)}):\n"
    if function_name == 'square':
        body = f"    return {parameters[0]} ** 2\n"
    else:
        random_operation = random.choice(['+', '-', '*', '/'])
        body = f"    return {parameters[0]} {
            random_operation} {parameters[0]}\n"
    code += body
    return code


function_name = 'square'
parameters = ['x']
generated_code = generate_code(function_name, parameters)
print(generated_code)
