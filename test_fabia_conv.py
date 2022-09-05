import unittest
from numericalunits import km, m, cm, mm
from fabia_conv import conv_len, fabia_length


class Test(unittest.TestCase):

    def test(self):
        self.assertEqual(conv_len(-1 * m), "to není ani čtvrt fabie")
        self.assertEqual(conv_len(-10 * m), "to není ani čtvrt fabie")
        self.assertEqual(conv_len(-100 * m), "to není ani čtvrt fabie")

        self.assertEqual(conv_len(0 * m), "to není ani čtvrt fabie")
        self.assertEqual(conv_len(1 * m), "to je asi čtvrt fabie")
        self.assertEqual(conv_len(2 * m), "to je asi půl fabie")
        self.assertEqual(conv_len(3 * m), "to je asi tři čtvrtě fabie")
        self.assertEqual(conv_len(4 * m), "to je asi jedna fabie")
        self.assertEqual(conv_len(5 * m), "to je asi jedna a čtvrt fabie")
        self.assertEqual(conv_len(6 * m), "to je asi jedna a půl fabie")
        self.assertEqual(conv_len(7 * m), "to je asi jedna a tři čtvrtě fabie")
        self.assertEqual(conv_len(8 * m), "to jsou asi 2 fabie")
        self.assertEqual(conv_len(9 * m), "to jsou asi 2 a čtvrt fabie")
        self.assertEqual(conv_len(10 * m), "to jsou asi 2 a půl fabie")
        self.assertEqual(conv_len(11 * m), "to jsou asi 2 a tři čtvrtě fabie")
        self.assertEqual(conv_len(12 * m), "to jsou asi 3 fabie")
        self.assertEqual(conv_len(16 * m), "to jsou asi 4 fabie")
        self.assertEqual(conv_len(20 * m), "to je asi 5 fabií")
        self.assertEqual(conv_len(21 * m), "to je asi 5 a čtvrt fabií")
        
        self.assertEqual(conv_len(0.1 * m), "to není ani čtvrt fabie")
        self.assertEqual(conv_len(0.4 * m), "to není ani čtvrt fabie")
        self.assertEqual(conv_len(0.5 * m), "to není ani čtvrt fabie")
        self.assertEqual(conv_len(0.7 * m), "to není ani čtvrt fabie")
        self.assertEqual(conv_len(0.9 * m), "to není ani čtvrt fabie")
        self.assertEqual(conv_len(1.3 * m), "to je asi čtvrt fabie")
        self.assertEqual(conv_len(1.5 * m), "to je asi půl fabie")
        self.assertEqual(conv_len(2.4 * m), "to je asi půl fabie")
        self.assertEqual(conv_len(2.5 * m), "to je asi tři čtvrtě fabie")

        self.assertEqual(conv_len(78 * m), "to je asi 19 a tři čtvrtě fabií")
        self.assertEqual(conv_len(79 * m), "to je asi 20 fabií")
        self.assertEqual(conv_len(80 * m), "to je asi 20 fabií")
        self.assertEqual(conv_len(82 * m), "to je asi 20 fabií")
        self.assertEqual(conv_len(100 * m), "to je asi 25 fabií")
        self.assertEqual(conv_len(110 * m), "to je asi 27 fabií")
        self.assertEqual(conv_len(120 * m), "to je asi 30 fabií")
        self.assertEqual(conv_len(1200 * m), "to je asi 303 fabií")
        self.assertEqual(conv_len(1201 * m), "to je asi 303 fabií")
        self.assertEqual(conv_len(120100 * m), "to je asi 30328 fabií")

        self.assertEqual(conv_len(4000 * mm), "to je asi jedna fabie")
        self.assertEqual(conv_len(400 * cm), "to je asi jedna fabie")
        self.assertEqual(conv_len(0.004 * km), "to je asi jedna fabie")
        self.assertEqual(conv_len(4 * km), "to je asi 1010 fabií")


        self.assertEqual(conv_len(fabia_length * 0.01), "to není ani čtvrt fabie")
        self.assertEqual(conv_len(fabia_length * 0.24), "to není ani čtvrt fabie")

        self.assertEqual(conv_len(fabia_length * 0.25), "to je asi čtvrt fabie")
        self.assertEqual(conv_len(fabia_length * 0.37), "to je asi čtvrt fabie")

        self.assertEqual(conv_len(fabia_length * 0.38), "to je asi půl fabie")
        self.assertEqual(conv_len(fabia_length * 0.62), "to je asi půl fabie")

        self.assertEqual(conv_len(fabia_length * 0.63), "to je asi tři čtvrtě fabie")
        self.assertEqual(conv_len(fabia_length * 0.87), "to je asi tři čtvrtě fabie")

        self.assertEqual(conv_len(fabia_length * 0.88), "to je asi jedna fabie")
        self.assertEqual(conv_len(fabia_length * 1.12), "to je asi jedna fabie")

        self.assertEqual(conv_len(fabia_length * 1.13), "to je asi jedna a čtvrt fabie")


if __name__ == '__main__':
    unittest.main()
