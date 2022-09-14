from numericalunits import km, cm
from extract import extract
from fabia_conv import conv_len

FOOTER = "^(Jsem jen robot a pokud jsem řekl nějakou hovadinu, tak se omlouvám.)\n"


def format_comment(lst):
    if not lst:
        return None
    return "".join(lst + [FOOTER])


def format_tuple(tupl):
    return f">{tupl[0]}\n\n{tupl[1]}\n\n"


def convert_tuple(tupl):
    return (tupl[0], conv_len(tupl[1]))


def is_good_size(tupl):
    return tupl[1] > 75 * cm and tupl[1] < 10 * km


def get_reply(text):
    return format_comment(
        list(map(format_tuple, map(convert_tuple, filter(is_good_size, extract(text)))))
    )
