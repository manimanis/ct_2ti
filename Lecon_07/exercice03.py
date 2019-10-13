# Affichage de la table de multiplication

n = int(input('Donner n : '))

for i in range(n+1):
    if i == 0:
        print('%2s' % ('*',), end='')
    else:
        print('%4d' % (i,), end='')
print()

for i in range(1, n+1):
    print('%2d' % i, end='')
    for j in range(1, n+1):
        print('%4d' % (i*j,), end='')
    print()
