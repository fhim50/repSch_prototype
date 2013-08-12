import unittest

from twitter import is_new

class TestTwitter(unittest.TestCase):

	def test_is_new(self):
		self.assertTrue(is_new('gsts',{'gsts':120,'academy':34}))
		self.assertFalse(is_new('popjohns',{'gsts':120,'academy':34}))

	def test_new_entry(self):
		self.assertEqual(new_entry('gsts',{}))



if __name__ == '__main__':
	unittest.main()