def time_to_min(time):
    """Convertit un temps au format 'hh:mm' en un nombre de minutes."""
    hh = int(time[:2])
    mm = int(time[3:])
    return 60 * hh + mm


def min_to_time(min):
    """Convertit un nombre de minutes en une heure au format 'hh:mm' """
    hh = min // 60, 
    mm = min % 60
    return '%02d:%02d' % (hh, mm)


def saisie_heure(msg, hdm):
    """"""
    while True:
        heure = input(msg)
        valide = len(heure) == 5 and heure[2] == ':'
        if valide:
            hh = int(heure[:2])
            mm = int(heure[3:])
            valide = 0 <= hh <= 23 and 0 <= mm <= 59
        if valide:
            valide = heure >= hdm
        if valide:
            return heure
        print('Saisie incorrecte.')


# Heures de révision de Physique
hd1 = saisie_heure("Heure début de révision (Physique) : ", '00:00')
hf1 = saisie_heure("Heure fin de révision (Physique) : ", hd1)

# Heures de révision de Math
hd2 = saisie_heure("Heure début de révision (Mathématiques) : ", hf1)
hf2 = saisie_heure("Heure fin de révision (Mathématiques) : ", hd2)

# Calculer la durée de révision de Physique en minutes
tr1 = time_to_min(hf1) - time_to_min(hd1)
# Calculer la durée de révision de Math en minutes
tr2 = time_to_min(hf2) - time_to_min(hd2)
# Calculer la durée totale de révision en minutes
tt = tr1 + tr2

# Affichage des résultats
print('Temps de révision')
print('Physique : ', min_to_time(tr1))
print('Math : ', min_to_time(tr2))
print('Durée Totale : ', min_to_time(tt))