from numericalunits import km, m, cm, mm

import re

regex = re.compile(r"""
        (?P<num>\d+([.,]\d{1,3})?)
        [ ]?
        (?P<unit>[cmk]?m(?=[ ,.?!;:]|$)|metr[ůyu]?|meters?)
        """, re.X)

def extract(text):
    return list(map(convert, re.finditer(regex, text)))

def convert(match):
    return (match.group(), num(match.group('num')) * unit(match.group('unit')))

def num(n):
    return float(n.replace(',','.'))

def unit(u):
    if re.match(r'^mm', u):
      return mm
    if re.match(r'^cm', u):
      return cm
    if re.match(r'^km', u):
      return km
    if re.match(r'^m|metr[ůyu]?|meters?$', u):
      return m

  
