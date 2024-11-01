import cmath

input_ = input()

input = input_.replace(' ', '')

input_ = input_.replace('+-', '-')
input_ = input_.replace('--', '+')

if 'j' not in input_:
    input_ += '+0j'
    
num = complex(input_)

modulus = abs(num)
argument = cmath.phase(num)

print(modulus)
print(argument)