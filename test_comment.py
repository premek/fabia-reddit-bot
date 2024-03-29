import unittest
from comment import get_reply, FOOTER


class Test(unittest.TestCase):
    def asrt(self, comment_text, expected):
        exp = None if expected is None else (expected + "\n\n" + FOOTER)
        self.assertEqual(get_reply(comment_text), exp)

    def test_m(self):
        self.asrt("", None)
        self.asrt(
            "nemovitost co tehdy stála 7 M, by teď stála třeba 8,5 M, takže", None
        )
        self.asrt("used 1.5mm² CU wire", None)

        self.asrt("1metr", ">1metr\n\nto je asi čtvrt fabie")
        self.asrt("1 metr", ">1 metr\n\nto je asi čtvrt fabie")
        self.asrt("1 m", ">1 m\n\nto je asi čtvrt fabie")
        self.asrt("1m.", ">1m\n\nto je asi čtvrt fabie")

        self.asrt(
            "jeden cyklista + 1.5 metr odstup", ">1.5 metr\n\nto je asi půl fabie"
        )
        self.asrt(
            "třeba klidně 100 m, přibližujeme",
            ">100 m\n\nto je asi 25 fabií",
        )
        self.asrt(
            "Windmill with height of 80m had to be at least 800 meters away",
            ">80m\n\nto je asi 20 fabií\n\n>800 meters\n\nto je asi 202 fabií",
        )

        self.asrt("Měřím 192 cm a prostě", ">192 cm\n\nto je asi půl fabie")
        self.asrt(
            "mám skoro 2 metry, ex měla 150 cm a stalo se",
            ">2 metry\n\nto je asi půl fabie",
        )
        self.asrt(
            "staré domy zdi třeba 800 mm i klidně metr, a nebo jestli mají zdi 3400 mm.",
            ">800 mm\n\nto není ani čtvrt fabie\n\n>3400 mm\n\nto je asi tři čtvrtě fabie",
        )

        self.asrt("749 mm", None)
        self.asrt("751 mm", ">751 mm\n\nto není ani čtvrt fabie")
        self.asrt(
            "třeba 800 mm, a nebo jestli mají zdi 400 mm.",
            ">800 mm\n\nto není ani čtvrt fabie",
        )

        self.asrt("9999 m", ">9999 m\n\nto je asi 2525 fabií")
        self.asrt("10001 m", None)

        self.asrt(
            "5 km 3 km 3 km",
            ">5 km\n\nto je asi 1262 fabií\n\n>3 km\n\nto je asi 757 fabií",
        )
        self.asrt("176cm 178 cm", ">176cm\n\nto je asi půl fabie")
