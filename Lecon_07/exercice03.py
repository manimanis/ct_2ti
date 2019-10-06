def table_mul(n):
    print('% 4s' % '*', end='')
    for j in range(n):
        print('% 4d' % (j+1), end='')
    print()

    for j in range(n):
        print('% 4d' % (j+1), end='')
        for i in range(n):
            print('% 4d' % ((i+1)*(j+1),), end='')
        print()


n = int(input('Donner n : '))
table_mul(n)
