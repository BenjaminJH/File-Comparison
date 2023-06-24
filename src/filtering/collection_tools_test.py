import unittest
from collection_tools import get_list_differences, get_dict_differences, get_dict_intersecting_keys


class TestCollectionTools(unittest.TestCase):
	example_list_a = [1, "2", int]
	example_list_b = [int, "3", 1, 5]
	example_dict_a = {"keyA": 0, "keyB": 0}
	example_dict_b = {"keyB": 0, "keyC": 0}

	def test_get_list_differences(self):
		a_only, b_only = get_list_differences(self.example_list_a, self.example_list_b)
		self.assertIn("2", a_only)
		self.assertIn("3", b_only)
		self.assertIn(5, b_only)

	def test_get_dict_differences(self):
		dict1_only, dict2_only = get_dict_differences(self.example_dict_a, self.example_dict_b)
		self.assertIn("keyA", dict1_only)
		self.assertIn("keyC", dict2_only)

	def test_get_dict_intersecting_keys(self):
		intersection = get_dict_intersecting_keys(self.example_dict_a, self.example_dict_b)
		self.assertEqual(["keyB"], intersection)


if __name__ == '__main__':
	unittest.main()
