import unittest
from numericalunits import km, m, cm, mm
from comment import get_reply, footer


class Test(unittest.TestCase):


    def test_m(self):
        self.assertEqual(get_reply(""), None)
        self.assertEqual(get_reply("nemovitost co tehdy stála 7 M, by teď stála třeba 8,5 M, takže"), None)
        self.assertEqual(get_reply("used 1.5mm² CU wire"), None)

        self.assertEqual(get_reply("1metr"), '>1metr\n\nto je asi čtvrt fabie\n\n' + footer)
        self.assertEqual(get_reply("1 metr"), '>1 metr\n\nto je asi čtvrt fabie\n\n' + footer)
        self.assertEqual(get_reply("1 m"), '>1 m\n\nto je asi čtvrt fabie\n\n' + footer)
        self.assertEqual(get_reply("1m."), '>1m\n\nto je asi čtvrt fabie\n\n' + footer)

        self.assertEqual(get_reply("jeden cyklista + 1.5 metr odstup"), '>1.5 metr\n\nto je asi půl fabie\n\n' + footer)
        self.assertEqual(get_reply("třeba klidně 100 m, přibližujeme"), '>100 m\n\nto je asi 25 fabií\n\n' + footer)
        self.assertEqual(get_reply("Windmill with height of 80m had to be at least 800 meters away"), '>80m\n\nto je asi 20 fabií\n\n>800 meters\n\nto je asi 202 fabií\n\n' + footer)

        self.assertEqual(get_reply("Měřím 192 cm a prostě"), '>192 cm\n\nto je asi půl fabie\n\n' + footer)
        self.assertEqual(get_reply("mám skoro 2 metry, ex měla 150 cm a stalo se"), '>2 metry\n\nto je asi půl fabie\n\n>150 cm\n\nto je asi půl fabie\n\n' + footer)
        self.assertEqual(get_reply("staré domy zdi třeba 800 mm i klidně metr, a nebo jestli mají zdi 3400 mm."), '>800 mm\n\nto není ani čtvrt fabie\n\n>3400 mm\n\nto je asi tři čtvrtě fabie\n\n' + footer)

        self.assertEqual(get_reply("749 mm"), None)
        # self.assertEqual(get_reply("750 mm"), None)  # FIXME different result every time
        self.assertEqual(get_reply("751 mm"), '>751 mm\n\nto není ani čtvrt fabie\n\n' + footer)
        self.assertEqual(get_reply("třeba 800 mm, a nebo jestli mají zdi 400 mm."), '>800 mm\n\nto není ani čtvrt fabie\n\n' + footer)

        self.assertEqual(get_reply("9999 m"), '>9999 m\n\nto je asi 2525 fabií\n\n' + footer)
        self.assertEqual(get_reply("10000 m"), None)

#TODO
#    def test_h(self):
#        self.assertEqual(get_reply("za cca 3 hodiny,"), '>3 hodiny\n\nto je asi 6 piv\n\n' + footer)
#        self.assertEqual(get_reply("Avia u Znojma ma dokonce za 37Kc"), '>37Kc\n\nto je asi jedno pivo\n\n' + footer)

# za 2 pizzy a 4 piva,
# dvě piva místo jednoho
# když si v hospodě po pěti pivech vyhlídneš slabšího jedince
# zbytkac o sile 3 piv.
# po 3 pivach :)
# aspoň 3piva.
# čtyři pětky za pivo
# 364 pivek
# jedno pivo
# Měl jsem dnes 5 piv, 
# Benzin stál 30 Kč, pivo 27,

# A to, že 178 cm je přesná šířka Fabie IV, neřekneš.
#5 km to je asi 1262 fabií 3 km to je asi 757 fabií 3 km to je asi 757 fabií  -- neopakovat stejne..
# 176cm je pul fab, 178 cm je pul fab - neopakovat pokud vysledek je stejny


if __name__ == '__main__':
    unittest.main()
