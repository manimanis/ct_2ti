# Conversion de température

# Saisie de la température
t = input('Donner une température en °C/°F (exemple : 15C) : ')

# extraire les chiffres et l'unité
t1, u1 = float(t[:-1]), t[-1]

if u1 == 'C':  # si la température en °C --> °F
    t2 = 9/5*t1+32
    u2 = 'F'
elif u1 == 'F':  # si la température en °F --> °C
    t2 = 5/9*(t1-32)
    u2 = 'C'

# Afficher le résultat
print(t1, u1, '=', t2, u2)
