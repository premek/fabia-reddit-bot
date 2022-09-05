from extract import extract
from fabia_conv import conv_len 
from numericalunits import km, m, cm, mm

footer = "^(Jsem jen robot a pokud jsem řekl nějakou hovadinu, tak se omlouvám.)\n"

def format_comment(lst):
    if lst:
        return ''.join(lst+[footer])

def format_tuple(t): 
    return f'>{t[0]}\n\n{t[1]}\n\n'

def convert_tuple(t):
    return (t[0], conv_len(t[1]))

def is_good_size(t):
    return t[1] > 75*cm and t[1] < 10*km

def get_reply(text):
    return format_comment(list(map(format_tuple, map(convert_tuple, filter(is_good_size, extract(text))))))

