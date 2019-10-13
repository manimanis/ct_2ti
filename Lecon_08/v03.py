
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


# Heures de révision de Physique
hd1, hf1 = saisie_revision("Physiques", '00:00')

# Heures de révision de Math
hd2, hf2 = saisie_revision("Mathématiques", hf1)

# Calculer la durée de révision de Physique en minutes
tr1 = time_to_min(hf1) - time_to_min(hd1)
# Calculer la durée de révision de Math en minutes
tr2 = time_to_min(hf2) - time_to_min(hd2)
# Calculer la durée totale de révision en minutes
tt = tr1 + tr2

# Affichage des résultats
print('Temps de révision')
print('Physique :', min_to_time(tr1))
print('Math :', min_to_time(tr2))
print('Durée Totale :', min_to_time(tt))
