from prime_number import prime_nums
import unittest
class GeneratePrimeNumbersTestCases(unittest.TestCase):
	def test_for_negative_input(self):
		result=prime_nums(-6)
		self.assertEqual(result,'Cannot generate prime numbers for negative integers')
	def test_for_invalid_input(self):
		with self.assertRaises(ValueError):
			result=prime_nums('h')
	def test_integer_one(self):
		result=prime_nums(1)
		self.assertEqual(result,'Zero or one cannot be a prime number' )
	def test_integer_zero(self):
		result=prime_nums(0)
		self.assertEqual(result,'Zero or one cannot be a prime number')
	def test_returns_a_list_of_generated_prime_numbers(self):
		result=prime_nums(10) 
		self.assertEqual(result,[3, 5, 7, 9],'Should return a list of prime number from zero to 10')

if __name__ == "__main__":
    unittest.main()