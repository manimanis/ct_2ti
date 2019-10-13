
def time_to_min(time):
    """Convertit un temps au format 'hh:mm' en un nombre de minutes."""
    hh = int(time[:2])
    mm = int(time[3:])
    return 60 * hh + mm


def min_to_time(min):
    """Convertit un nombre de minutes en une heure au format 'hh:mm' """
    hh, mm = min // 60, min % 60
    return '%02d:%02d' % (hh, mm)


def saisie_heure(msg, hdm):
    """Assure la saisie d'une date valide qui :
    - respecte le format 'hh:mm'
    - est dans l'intervalle '00:00' à '23:59'
    - est supèrieure ou égale à hdm."""
    while True:
        hd = input(msg)
        if len(hd) != 5 or \
                hd[2] != ':' or \
                not hd[:2].isdigit() or \
                not hd[3:].isdigit():
            print('Format incorrect!')
            continue

        if 0 > int(hd[:2]) or int(hd[:2]) > 23 or \
                0 > int(hd[3:]) or int(hd[3:]) > 59:
            print('Date incorrecte!')
            continue

        if hd < hdm:
            print("L'heure doit être >=", hdm)
            continue

        return hd


def saisie_revision(matiere, hdm):
    """Saisie de l'heure de début et de fin de révision d'une seule matière."""
    while True:
        hdr = saisie_heure(
            "Heure début de révision (%s) >= %s : " % (matiere, hdm), hdm)
        hfr = saisie_heure("Heure de fin de révision (%s) > %s : " %
                           (matiere, hdr), hdr)

        if hfr > hdr:
            return hdr, hfr
        else:
            print("L'heure de fin de révision doit être >", hdr)


# Saisie du nombre de matières
n = int(input('Donner le nombre de matières à réviser : '))

l_revision = []
trt = 0
hdm = '00:00'
for i in range(n):
    print('Matière n°', (i+1))

    # Matière à réviser
    matiere = input('Donner le nom de la matière : ')

    # Heures de révision de Physique
    hdr, hfr = saisie_revision(matiere, hdm)

    # Temps de révision
    trm = time_to_min(hfr) - time_to_min(hdr)

    # Temps de révision total
    trt += trm

    # ajouter le nom de la matière
    # et le temps de révision
    l_revision.append((matiere, trm))

    hdm = hfr

# Affichage des résultats
print('Temps de révision')
for matiere, tr in l_revision:
    print(matiere, ':', min_to_time(tr))

print('Durée Totale :', min_to_time(trt))
