import unittest
from collection_tools import get_list_differences, get_dict_differences, get_dict_intersecting_keys, \
	get_dict_where_value_differs


class TestCollectionTools(unittest.TestCase):
	example_list_a = [1, "2", int]
	example_list_b = [int, "3", 1, 5]
	example_dict_a = {"keyA": 1, "keyB": 2}
	example_dict_b = {"keyB": 4, "keyC": 1}

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

	def test_get_dict_where_value_differs(self):
		key_found_different_values = get_dict_where_value_differs(self.example_dict_a, self.example_dict_b)
		self.assertEqual({"keyB": (2, 4)}, key_found_different_values)


if __name__ == '__main__':
	unittest.main()
