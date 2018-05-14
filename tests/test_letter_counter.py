import unittest
import unittest.mock
from letter_counter import *

class TestLetterCounter( unittest.TestCase ):
    
    def test_getTotalOccurences( self ):
        with self.subTest( "phrase has all letters"):
            result = getTotalOccurrencesOfLettersToCount("aabbaacc", "abc")
            self.assertEquals( result, 8 )

        with self.subTest( "phrase has no letters"):
            result = getTotalOccurrencesOfLettersToCount("aabbaacc", "xyz")
            self.assertEquals( result, 0 )

    def test_inputPhrase( self ):
        with unittest.mock.patch( 'builtins.input', return_value ="the phrase"):
            self.assertEquals( getInputPhrase(), "the phrase")