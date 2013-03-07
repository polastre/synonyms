import unittest
import synonyms
import os

synfile = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'syn.txt')

class TestSyn(unittest.TestCase):
    def test_load_list(self):
        f = [['USA', 'United States'],
             ['Rock','boulder', 'pebble']]
        s = synonyms.load(f)
        self.assertEqual(s.match('boulder'), 'rock')

    def test_load_file(self):
        fp = open(synfile)
        s = synonyms.load(fp)
        self.assertEqual(s.match('boulder'), 'rock')

    def test_load_str(self):
        fp = open(synfile)
        f = fp.read()
        s = synonyms.load(f)
        self.assertEqual(s.match('boulder'), 'rock')

    def test_in(self):
        s = synonyms.load(open(synfile))
        self.assertTrue('uSa' in s)

    def test_ignorecase_true_1(self):
        s = synonyms.load(open(synfile))
        self.assertEqual(s.match('BoulDer'), 'rock')

    def test_ignorecase_true_2(self):
        s = synonyms.load(open(synfile))
        self.assertEqual(s.match('united states'), 'usa')

    def test_ignorecase_false_1(self):
        s = synonyms.load(open(synfile), ignoreCase=False)
        self.assertEqual(s.match('BoulDer'), None)

    def test_ignorecase_false_2(self):
        s = synonyms.load(open(synfile), ignoreCase=False)
        self.assertEqual(s.match('Rock'), 'Rock')

if __name__ == '__main__':
    unittest.main()
