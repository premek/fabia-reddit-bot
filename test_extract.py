import unittest
from numericalunits import km, m, cm, mm
from extract import extract


class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(extract(""), [])

        # self.assertEqual(extract("metr"), [("metr", 1*m)])
        self.assertEqual(extract("1metr"), [("1metr", 1 * m)])
        self.assertEqual(extract("1 metr"), [("1 metr", 1 * m)])
        self.assertEqual(extract("1 m"), [("1 m", 1 * m)])
        self.assertEqual(extract("1 m."), [("1 m", 1 * m)])

        self.assertEqual(extract("kazdych 30m je krizovatka"), [("30m", 30 * m)])
        self.assertEqual(extract("max 1.6m long"), [("1.6m", 1.6 * m)])
        self.assertEqual(
            extract("jeden cyklista + 1.5 metr odstup"), [("1.5 metr", 1.5 * m)]
        )
        self.assertEqual(extract("1,5 metru odstup"), [("1,5 metru", 1.5 * m)])
        self.assertEqual(extract("200 metrů"), [("200 metrů", 200 * m)])
        self.assertEqual(extract("50 metry"), [("50 metry", 50 * m)])
        self.assertEqual(extract("63 metru a na druhou 75,"), [("63 metru", 63 * m)])
        self.assertEqual(extract("asi 2 metry od mě"), [("2 metry", 2 * m)])
        self.assertEqual(extract("cca 1m od kraje,"), [("1m", 1 * m)])
        self.assertEqual(
            extract("třeba klidně 100 m, přibližujeme"), [("100 m", 100 * m)]
        )
        self.assertEqual(
            extract("Windmill with height of 80m had to be at least 800 meters away"),
            [("80m", 80 * m), ("800 meters", 800 * m)],
        )

        self.assertEqual(extract("1000 km"), [("1000 km", 1000 * km)])
        self.assertEqual(extract("Měřím 192 cm a prostě"), [("192 cm", 192 * cm)])
        self.assertEqual(extract("strojkem jedu 5 mm vše."), [("5 mm", 5 * mm)])
        self.assertEqual(
            extract("mám skoro 2 metry, ex měla 150 cm a stalo se"),
            [("2 metry", 2 * m), ("150 cm", 150 * cm)],
        )
        self.assertEqual(
            extract("mám skoro 2000 mm, ex měla 150 cm."),
            [("2000 mm", 2000 * mm), ("150 cm", 150 * cm)],
        )
        self.assertEqual(extract("Maybe like 5cm of snow."), [("5cm", 5 * cm)])
        self.assertEqual(
            extract(
                "staré domy zdi třeba 800 mm i klidně metr, a nebo jestli mají zdi 400 mm."
            ),
            [("800 mm", 800 * mm), ("400 mm", 400 * mm)],
        )

        self.assertEqual(
            extract("nemovitost co tehdy stála 7 M, by teď stála třeba 8,5 M, takže"),
            [],
        )
        self.assertEqual(extract("used 1.5mm² CU wire"), [])
