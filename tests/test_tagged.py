'''
Created on 11.02.2013

@author: nimrod
'''
import unittest

from wvtagconvert import parse_input

from samples import vcards, tags

class VcardParserTest(unittest.TestCase):
    """ Some very lousy initial test cases """
    def runTest(self):
        teststr = '\n* '.join(vcards)
        res = parse_input(teststr, 'vcard')
        self.assertEqual(len(res), len(vcards))
        for r in res:
            self.assertIn('type', r)
            self.assertIn('name', r)


class TagParserTest(unittest.TestCase):
    def runTest(self):
        teststr = '\n* '.join(tags)
        res = parse_input(teststr, 'vcard')
        self.assertEqual(len(res), len(tags))
        for r in res:
            self.assertIn('type', r)
            self.assertIn('name', r)



if __name__ == "__main__":
    unittest.main(verbosity=2)