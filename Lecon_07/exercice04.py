def f_to_c(f):
    return 5/9*(f-32)


def c_to_f(c):
    return 9/5*c+32


temp = input('Donner la température : ')
t, u = float(temp[:-1]), temp[-1].upper()
if temp[-1] == 'F':
    print('{}°F = {}°C'.format(t, f_to_c(t)))
else:
    print('{}°C = {}°F'.format(t, c_to_f(t)))
