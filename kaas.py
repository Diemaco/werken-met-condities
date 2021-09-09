print('Welkom bij de \'Wie is het\' hard-coded editie!')


def stel_vraag(input_string):
    return input(input_string).lower().startswith('j')


def main_duidelijk():
    if stel_vraag('Is de kaas geel?'):
        if stel_vraag('Zitten er gaten in?'):
            if stel_vraag('Is de kaas belachelijk duur?'):
                return 'Emmenthaler'
            else:
                return 'Leerdammer'
        else:
            if stel_vraag('Is de kaas hard als steen?'):
                return 'Parmigiano Reggiano'
            else:
                return 'Goudse kaas'
    else:
        if stel_vraag('Heeft de kaas blauwe schimmels?'):
            if stel_vraag('Heeft de kaas een korst?'):
                return 'Blue de Rochbaron'
            else:
                return 'Foume d\'Ambert'
        else:
            if stel_vraag('Heeft de kaas een korst?'):
                return 'Camembert'
            else:
                return 'Mozzarella'


def main_simpeler():
    if stel_vraag('Is de kaas geel?'):
        if stel_vraag('Zitten er gaten in?'):
            if stel_vraag('Is de kaas belachelijk duur?'):
                return 'Emmenthaler'
            else:
                return 'Leerdammer'
        elif stel_vraag('Is de kaas hard als steen?'):
            return 'Parmigiano Reggiano'
        else:
            return 'Goudse kaas'
    elif stel_vraag('Heeft de kaas blauwe schimmels?'):
        if stel_vraag('Heeft de kaas een korst?'):
            return 'Blue de Rochbaron'
        else:
            return 'Foume d\'Ambert'
    elif stel_vraag('Heeft de kaas een korst?'):
        return 'Camembert'
    else:
        return 'Mozzarella'


if __name__ == '__main__':
    print(f'Mijn kaas was \'{main_simpeler()}\'')
