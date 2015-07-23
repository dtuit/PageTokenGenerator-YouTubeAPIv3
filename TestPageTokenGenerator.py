import unittest
import PageTokenGenerator

class TestPageTokenGenerator(unittest.TestCase):

	''' indices where the Sequence Changes'''
	known_tokens = (
		(0	  ,"CAAQAA"),
		(127  ,"CH8QAA"),
		(128  ,"CIABEAA"),
		(129  ,"CIEBEAA"),
		(8191 ,"CP8_EAA"),
		(8192 ,"CIBAEAA"),
		(8193 ,"CIFAEAA"),
		(16383,"CP9_EAA" ),
		(16384,"CICAARAA"),
		(16385,"CIGAARAA"),
		(24575,"CP-_ARAA"),
		(24576,"CIDAARAA"),
		(24577,"CIHAARAA"),
		(32767,"CP__ARAA"),
		(32768,"CICAAhAA"),
		(32769,"CIGAAhAA"),
		(40959,"CP-_AhAA"),
		(40960,"CIDAAhAA"),
		(40961,"CIHAAhAA"),
		(49151,"CP__AhAA"),
		(49152,"CICAAxAA"),
		(49153,"CIGAAxAA"),
		(57343,"CP-_AxAA"),
		(57344,"CIDAAxAA"),
		(57345,"CIHAAxAA"),
		(65535,"CP__AxAA"),
		(65536,"CICABBAA"),
		(65537,"CIGABBAA"),
		(73727,"CP-_BBAA"),
		(73728,"CIDABBAA"),
		(73729,"CIHABBAA"),
		(81919,"CP__BBAA"),
		(81920,"CICABRAA"),
		(81921,"CIGABRAA"),
		(90111,"CP-_BRAA"),
		(90112,"CIDABRAA"),
		(90113,"CIHABRAA"),
		(98303,"CP__BRAA"),
		(98304,"CICABhAA"),
		(98305,"CIGABhAA"),
		(99999,"CJ-NBhAA")
	)

	def test_correctTokens(self):
		''' PageTokenGenerator Should give output known token with known input '''
		for integer, token in self.known_tokens:
			result = PageTokenGenerator.number_to_token(integer)
			self.assertEqual(token, result)

if __name__ == '__main__':
    unittest.main()