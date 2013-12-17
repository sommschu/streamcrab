from unittest import TestCase
from smm.classifier.textprocessing import StopStemmTwitterProcessor
__author__ = 'gx'


class TestStopStemmTwitterProcessor(TestCase):

    def setUp(self):
        self.text =  "The quick brown fox was jumping over the lazy dog #crazyfox @thedog http://fox.com :)"

    def test_getClean(self):
        self.assertEqual("the quick brown fox was jumping over the lazy dog #crazyfox @thedog http://fox.com  __h__", StopStemmTwitterProcessor.clean(self.text))

    def test_getClassifierTokens(self):
        self.assertEqual(['quick', 'brown', 'fox', 'jump', 'lazi', 'dog', '#crazyfox', '__h__'], StopStemmTwitterProcessor.getClassifierTokens(self.text))