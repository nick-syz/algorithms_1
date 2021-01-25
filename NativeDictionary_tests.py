from NativeDictionary import NativeDictionary
from unittest import TestCase

class NativeDictionaryTest(TestCase):
    def setUp(self):
        self.dict = NativeDictionary(11)
    
    def test_is_key(self):
        self.assertEqual(False, self.dict.is_key('Some'))

    def test_put(self):
        self.dict.put('One_k', 'One_v')
        self.assertEqual(True, self.dict.is_key('One_k')) # True
        
        self.dict.put('Two_k', 'Two_v')
        # self.assertEqual(True, self.dict.is_key('Two_v')) # False
        self.assertEqual(True, self.dict.is_key('Two_k'))

    def test_get(self):
        self.dict.put('Two_k', 'Two_v')
        self.assertEqual('Two_v', self.dict.get('Two_k'))
        self.dict.put('Three_k', 'Three_v')
        self.assertEqual('Three_v', self.dict.get('Three_k'))
