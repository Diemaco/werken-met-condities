def stel_vraag(input_string):
    return input(input_string).lower().startswith('j')


def main():
    genoeg_ervaring = True
    if float(input('Hoeveel jaren praktijkervaring heeft u met dieren-dressuur?\n')) <= 4:
        genoeg_ervaring = False

    if (not genoeg_ervaring) and (float(input('Hoeveel jaren ervaring heeft u met jongleren?\n')) <= 5):
        genoeg_ervaring = False

    if (not genoeg_ervaring) and (float(input('Hoeveel jaren praktijkervaring heeft u met acrobatiek?\n')) <= 3):
        genoeg_ervaring = False

    if not genoeg_ervaring:
        return 'Niet genoeg ervaring'

    if not stel_vraag('Heeft u een MBO-4 diploma? (J/N)\n'):
        return 'Geen MBO-4 diploma'

    if not stel_vraag('Bent u in bezit van een geldig vrachtwagen rijbewijs? (J/N)\n'):
        return 'Geen geldig vrachtwagen rijbewijs'

    if not stel_vraag(
            'Bent u in bezit van een hoge hoed die aan de volgende criteria voldoet:\n\t- Weegt minimaal 250 gram\n\t- Is zwart\n\t- Is belachelijk duur\n\t- Is een familie erfstuk \n(J/N)\n'):
        return 'Wie heeft dat nou niet?!?!? (Geen hoge hoed die de criteria voldoet)'

    voldoet_criteria = True
    if stel_vraag('Bent u een man? (J/N)\n'):
        if float(input('Hoe breedt is uw snor?\n')) <= 10:
            return 'Geen echte man'
    else:
        antwoord = input('Wat voor haar heeft u?\n').lower()
        if antwoord != 'krullend':
            return f'Sorry maar wij zoeken niet naar iemand met \'{antwoord}\' haar'
        if input('Welke kleur is uw haar?\n').lower() != 'rood':
            return 'ff haarverfen en terug komen'
        elif float(input('Hoe lang us uw haar in CM?\n')) <= 20:
            return 'Uw haar is niet goed genoeg voor dit werk'

    if float(input('Hoe lang bent u in cm?\n')) < 150:
        return 'Woah! Zo lang?!? Nee, sorry.'

    if float(input('Hoeveel KG weegt u?\n')) < 90:
        return 'Sorry, kom maar terug als je hetzelfde weegt als je moeder (>2^64KG)'

    if not stel_vraag('Heeft u het \'Overleven met gevaarlijk personeel\' certificaat (J/N)\n'):
        return 'Vanwegen het knuffelbeer personeel bij Circus HotelDeBotel is het te gevaarlijk om zonder certificaat hier te werken'

    if not stel_vraag('Heeft u uw teldiploma gekregen? (J/N)\n'):
        return 'Tel maar tot 5 en kom dan terug'

    if not stel_vraag('BELANGRIJK! Heeft u uw \'Naar de WC gaan\' diploma al gekregen? (J/N)\n'):
        return 'Hoe durf je zonder je \'Naar de WC gaan\' diploma naar ons toe te komen'

    if not stel_vraag('Wil je minder dan €4315321543265462^0 per week betaald worden? (J/N)\n'):
        return 'Kom maar terug als je niet zp hebberig bent'

    if stel_vraag('Komt u hier om serieus te werken of om spelletjes te gaan spelen? (J/N)\n'):
        return 'Oké, heel erg bedankt voor uw tijd.'


if __name__ == '__main__':
    print(main())
