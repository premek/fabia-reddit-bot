from numericalunits import m
from math import floor


fabia_length = 3.96 * m
#fabia_hatchback_trunk_volume = 260*l

def conv_len(length):
    if length < fabia_length/4:
        return "to není ani čtvrt fabie"

    value = length / fabia_length
    rounded = round(value * 4) / 4

    whole=floor(rounded)
    frac=rounded-whole

    je = "jsou" if whole >= 2 and whole <=4 else "je"
    wholeStr = "jedna" if whole==1 else str(whole)
    wholeAnd = f'{wholeStr} a ' if whole > 0 else ""

    fab = "fabií" if whole >= 5 else "fabie"

    if frac==0 or whole >= 20:
        return f'to {je} asi {wholeStr} {fab}'
    elif frac ==0.25:
        return f'to {je} asi {wholeAnd}čtvrt {fab}'
    elif frac ==0.5:
        return f'to {je} asi {wholeAnd}půl {fab}'
    elif frac ==0.75:
        return f'to {je} asi {wholeAnd}tři čtvrtě {fab}'
    else:
        return f'to {je} přibližně {whole} {fab}' # should not happen?

