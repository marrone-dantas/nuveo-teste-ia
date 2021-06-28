import unittest
import os
import inspect
import sys

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir) 

from src.SpamDetector.SpamDetector import SpamDetector

class TestPrediction(unittest.TestCase):

    def test_ham(self):

        detector = SpamDetector(0.5)

        detector.set_model('sms_model_v1.pkl')
        
        sms = 'Webpage s not available!'

        self.assertFalse(detector.is_spam(sms), "Should be True")

    def test_prob_ham(self):

        detector = SpamDetector(0.5)

        detector.set_model('sms_model_v1.pkl')
        
        sms = 'Webpage s not available!'

        self.assertLess(detector.prob_spam(sms), 0.5, "Should be less then 0.5")

    def test_spam(self):

        detector = SpamDetector(0.5)

        detector.set_model('sms_model_v1.pkl')
        
        sms = "8007 25p 4 Alfie Moon's Children in Need song on ur mob. Tell ur m8s. Txt TONE CHARITY to 8007 for nokias or POLY CHARITY for polys :zed 08701417012 profit 2 charity'"

        self.assertTrue(detector.is_spam(sms), "Should be False")

    def test_prob_spam(self):

        detector = SpamDetector(0.5)

        detector.set_model('sms_model_v1.pkl')
        
        sms = "8007 25p 4 Alfie Moon's Children in Need song on ur mob. Tell ur m8s. Txt TONE CHARITY to 8007 for nokias or POLY CHARITY for polys :zed 08701417012 profit 2 charity'"

        self.assertGreater(detector.prob_spam(sms), 0.5, "Should be greates then 0.5")

    def test_get_thresh(self):

        detector = SpamDetector(0.5)

        self.assertEquals(detector.get_thresh(), 0.5, "Should be equals 0.5")

    def test_set_thresh(self):

        detector = SpamDetector(0.5)

        detector.set_thresh(0.6)

        self.assertEquals(detector.get_thresh(), 0.6, "Should be equals 0.6")

if __name__ == '__main__':
    unittest.main()