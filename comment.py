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


# tuple (length_text, num*unit) => tuple (length_text, fabia_length_text)
def convert_tuple(tupl):
    return (tupl[0], conv_len(tupl[1]))


def is_good_size(tupl):
    return tupl[1] > 75 * cm and tupl[1] < 10 * km


# do not repeat when the converted value is the same
def uniq(tuples):
    unique = {}
    for tupl in tuples:
        if tupl[1] not in unique:
            unique[tupl[1]] = tupl
    return list(unique.values())


def get_reply(text):
    extracted = extract(text)
    filtered = filter(is_good_size, extracted)
    converted = list(map(convert_tuple, filtered))
    unique = uniq(converted)
    formatted = list(map(format_tuple, unique))
    return format_comment(formatted)
