import unittest
from postcode import *


class TestPostcodeMethods(unittest.TestCase):

   # Tests the functionality of Normalise with a random postcode
    def test_normalised_output(self):
        p = postcode()
        with self.assertRaises(Exception) as context:
            p.Normalise('')
            # Test Null
            self.assertTrue('Not allowed to normalise an empty postcode!' in context.exception)
        # Test Postcode
        self.assertEqual(p.Normalise('Ec1a 1bB'),'EC1A1BB')

    """
        There are 6 versions of postCodes to test of validity.
        The next 6 tests test each one individually. The test patterns
        are shown below:

        A. AA9A 9AA
        B. A9A 9AA
        C. A9 9AA
        D. A99 9AA
        E. AA9 9AA
        F. AA99 9AA
    """

    def test_verify_output(self):
        p = postcode()
        with self.assertRaises(Exception) as context:
            p.Verify('')
            # Test Null case
            self.assertTrue('Not allowed to normalise an empty postcode!' in context.exception)
        self.assertTrue(bool(p.Verify('Ec1a 1bB'))) #A
        self.assertTrue(bool(p.Verify('W1A 0ax')))  #B
        self.assertTrue(bool(p.Verify('M11aE')))    #C
        self.assertTrue(bool(p.Verify('b33 8tH')))  #D
        self.assertTrue(bool(p.Verify('CR26XH')))   #E
        self.assertTrue(bool(p.Verify('Dn551Pt')))  #F


    """
        The next tests check the error detection for invalid postCodes
        Each test is a tect for each position of the postcode
    """
    def test_verify_invalid_output(self):
        p = postcode()
        # Tests position 1 (not allowed QVX)
        self.assertFalse(bool(p.Verify('QC1A 1BB')))
        # Tests position 2 (not allowed IJZ)
        self.assertFalse(bool(p.Verify('EI1A 1BB')))
        # Tests position 3 (allowed ABCDEFGHJKPSTUW)
        self.assertFalse(bool(p.Verify('W1L 0AX')))
        # Tests position 4 (allowed ABEHMNPRVWXY)
        self.assertFalse(bool(p.Verify('EC1C 1BB')))
        # Tests position 5 (not allowed  CIKMOV)
        self.assertFalse(bool(p.Verify('EC1A 1MB')))
        # Tests position 6 (not allowed  CIKMOV)
        self.assertFalse(bool(p.Verify('EC1A 1BM')))


    """
        Tests inward function, as it is a fixed size (3) for Each
        postcode it can be tested with any postcode
    """
    def test_verify_inward_output(self):
        p = postcode()
        with self.assertRaises(Exception) as context:
            p.GetInward('')
            # Test Null
            self.assertTrue('Not allowed to normalise an empty postcode!' in context.exception)
        # Test correct case
        self.assertEqual(p.GetInward('EC1A 1BB'), '1BB')
        # Test Error Case
        self.assertFalse(p.GetInward('QQQ QQQ'))

    """
        Tests outward function, as it is a variable length 2-4 chars long
        each case must be tested
    """
    def test_verify_outward_output(self):
        p = postcode()
        with self.assertRaises(Exception) as context:
            p.GetOutward('')
            # Test Null case
            self.assertTrue('Not allowed to normalise an empty postcode!' in context.exception)
        #Test with 2 values in outward
        self.assertEqual(p.GetOutward('M1 1AE'), 'M1')
        #Test with 3 values in outward
        self.assertEqual(p.GetOutward('CR2 6XH'), 'CR2')
        #Test with 4 values in outward
        self.assertEqual(p.GetOutward('EC1A 1BB'), 'EC1A')
        # Tests invalid input on Outward
        self.assertFalse(p.GetOutward('QQQ QQQ'))

    """
        Tests PostCodeUnit function, as it is a fixed size (2) for Each
        postcode it can be tested with any postcode
    """

    def test_verify_PostcodeUnit_output(self):
            p = postcode()
            with self.assertRaises(Exception) as context:
                p.GetPostcodeUnit('')
                # Test Null case
                self.assertTrue('Not allowed to normalise an empty postcode!' in context.exception)
            # Test correct value
            self.assertEqual(p.GetPostcodeUnit('EC1A 1BB'), 'BB')
            #Test error case
            self.assertFalse(p.GetPostcodeUnit('QQQ QQQ'))

    """
        Tests PostCodeSector function, as it is a fixed size (1) for Each
        postcode it can be tested with any postcode
    """

    def test_verify_PostcodeSector_output(self):
        p = postcode()
        with self.assertRaises(Exception) as context:
            p.GetPostcodeSector('')
            # Test Null Case
            self.assertTrue('Not allowed to normalise an empty postcode!' in context.exception)
        #Test correct case
        self.assertEqual(p.GetPostcodeSector('EC1A 1BB'), '1')
        #Test incroorect case
        self.assertFalse(p.GetPostcodeSector('QQQ QQQ'))

    """
        Tests TestGetPostCodeArea function, as it is a variable length 1-2 chars long
        each case must be tested
    """
    def test_verify_PostcodeArea_output(self):
        p = postcode()
        with self.assertRaises(Exception) as context:
            p.GetPostcodeArea('')
            # Test Null Case
            self.assertTrue('Not allowed to normalise an empty postcode!' in context.exception)
        # Test Area with 1 letter
        self.assertEqual(p.GetPostcodeArea('B33 8TH'), 'B')
        # Test Area with 2 letters
        self.assertEqual(p.GetPostcodeArea('EC1A 1BB'), 'EC')
        #Test incroorect case
        self.assertFalse(p.GetPostcodeArea('QQQ QQQ'))

    """
        Tests TestGetPostCodeDistrict function, as it is a variable length 2-4 chars long
        each case must be tested
    """
    def test_verify_PostcodeDistrict_output(self):
        p = postcode()
        with self.assertRaises(Exception) as context:
            # Test Null case
            p.GetPostcodeDistrict('')
            self.assertTrue('Not allowed to normalise an empty postcode!' in context.exception)
            # Test District with 2 values 1 numer 1 letter
            self.assertEqual(p.GetPostcodeDistrict('EC1A 1BB'), '1A')
            # Test District with 2 values, 2 numbers
            self.assertEqual(p.GetPostcodeDistrict('B33 8TH'), '33')
            # Tests Invalid input on PostCodeDistrict
            self.assertFalse(p.GetPostcodeDistrict('QQQ QQQ'))



if __name__ == '__main__':
    unittest.main()
