def string_to_exp(exp_str):
    exp = {}
    exp_split = exp_str.split('^') # [2x]
    coeff_var,exp['exponent'] = exp_split if len(exp_split) > 1 else (exp_split,1)
    coeff_var = ''.join(coeff_var)
    if coeff_var[-1].isdigit():
        exp['var'] = ''
        exp['coeff'] = coeff_var
    else:
        exp['var'] = coeff_var[-1]
        exp['coeff'] = coeff_var[:-1]
    try:
        exp['coeff'] = int(exp['coeff']) if len(exp['coeff']) > 0 else 1
    except:
        exp['coeff'] = float(exp['coeff'])
    if exp['var'] == '' and exp['exponent'] == 1:
        exp['exponent'] = 0
    try:
        exp['exponent'] = int(exp['exponent'])
    except:
        exp['exponent'] = float(exp['exponent'])
    return exp

def exp_derivative(exp):
    new_exp = {}
    # the spelling of 'exp' is starting to look really weird
    new_exp['coeff'] = exp['coeff'] * exp['exponent']
    new_exp['exponent'] = exp['exponent'] - 1
    new_exp['var'] = exp['var']
    return new_exp

def exp_to_string(exp,order):
    if exp['coeff'] == 0:
        return ''
    string = ''
    if order != 0:
        string += ' + '
    string += str(exp['coeff']) if (exp['coeff'] != 1 or exp['exponent'] == 0) else ''
    string += str(exp['var']) if exp['exponent'] != 0 else ''
    string += ( '^' + str(exp['exponent'])) if exp['exponent'] != 0 and exp['exponent'] != 1 else ''
    return string

def derivative(eq):
    eq = eq.replace(' ','')
    exps = [string_to_exp(exp_str) for exp_str in eq.split('+')]
    new_exps = [exp_derivative(exp) for exp in exps]
    eq_strings = [exp_to_string(exp,i) for i,exp in enumerate(new_exps)]
    return ''.join(eq_strings)

# Gonna steal this from you Lexyth.... ty!
while True:
    try:
        expr = input()
        print(f'{expr} = {derivative(expr)}')
    except:
        break
'''
x^2 + 5x
3x^4 + 3
2.5x^4 + 5x^1.2 + 0x^10
5x^-1 + x^0.5
1 + x^2 + x
'''
# =>
'''
x^2 + 5x = 2x + 5
3x^4 + 3 = 12x^3
2.5x^4 + 5x^1.2 + 0x^10 = 10.0x^3 + 6.0x^0.19999999999999996
5x^-1 + x^0.5 = -5x^-2 + 0.5x^-0.5
1 + x^2 + x =  + 2x + 1
'''