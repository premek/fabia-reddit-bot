import re
from numericalunits import km, m, cm, mm


regex = re.compile(
    r"""
        (^|\b)
        (?P<text>
          (?P<num>\d+([.,]\d{1,3})?)
          [ ]?
          (?P<unit>[cmk]?m|metr[ůyu]?|meters?)
        )
        ([ ,.?!;:]|$)
        """,
    re.X,
)


# returns list of tuples (length_text, num*unit)
def extract(text):
    return list(map(convert, re.finditer(regex, text)))


def convert(match):
    return (
        match.group("text"),
        get_num(match.group("num")) * get_unit(match.group("unit")),
    )


def get_num(num):
    return float(num.replace(",", "."))


def get_unit(unit):
    if re.match(r"^mm", unit):
        return mm
    if re.match(r"^cm", unit):
        return cm
    if re.match(r"^km", unit):
        return km
    if re.match(r"^m|metr[ůyu]?|meters?$", unit):
        return m
    raise ValueError("unknown unit: " + unit)  # pragma: no cover
