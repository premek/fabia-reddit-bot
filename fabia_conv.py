from math import floor
from numericalunits import m


fabia_length = 3.96 * m
# fabia_hatchback_trunk_volume = 260*l


def conv_len(length):
    if length < fabia_length / 4:
        return "to není ani čtvrt fabie"

    value = length / fabia_length
    rounded = round(value * 4) / 4

    whole = floor(rounded)
    frac = rounded - whole

    jsou = "jsou" if 2 <= whole <= 4 else "je"
    whole_str = "jedna" if whole == 1 else str(whole)
    whole_and = f"{whole_str} a " if whole > 0 else ""

    fab = "fabií" if whole >= 5 else "fabie"

    if frac == 0 or whole >= 20:
        return f"to {jsou} asi {whole_str} {fab}"
    if frac == 0.25:
        return f"to {jsou} asi {whole_and}čtvrt {fab}"
    if frac == 0.5:
        return f"to {jsou} asi {whole_and}půl {fab}"
    if frac == 0.75:
        return f"to {jsou} asi {whole_and}tři čtvrtě {fab}"
    return f"to {jsou} přibližně {whole} {fab}"  # should not happen # pragma: no cover
