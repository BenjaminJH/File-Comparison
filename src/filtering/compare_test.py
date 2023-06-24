import unittest
import os
import test
from src.filtering.collection_tools import get_dict_differences
from src.filtering.compare import compare_by_file_path, compare_by_file_count, build_file_strings, PRIMARY_DIRECTORY, SECONDARY_DIRECTORY

path = os.path.dirname(test.__file__)
dir1 = path+"\\example_directories\\test_directory_a"
dir2 = path+"\\example_directories\\test_directory_b"


class TestCompare(unittest.TestCase):

	def test_compare_by_file_path(self):
		# TODO: maybe add some string io testing
		dir1_only, dir2_only = compare_by_file_path(dir1, dir2)
		dir1_only.sort()
		dir2_only.sort()
		expected_dir1 = ['\\file_c.txt', '\\subdirectory\\file_c.txt']
		expected_dir2 = ['\\subdirectory\\file_a.txt', '\\subdirectory\\deeper_directory\\file_a.txt', '\\file_b.txt']
		expected_dir1.sort()
		expected_dir2.sort()
		self.assertEqual(2, len(dir1_only))
		self.assertEqual(3, len(dir2_only))
		self.assertEqual(expected_dir1, dir1_only)
		self.assertEqual(expected_dir2, dir2_only)

	def test_compare_by_file_count(self):
		# TODO: maybe add some string io testing
		dict1_only, dict2_only = compare_by_file_count(dir1, dir2)
		expected_dir1 = {'file_c.txt': 2}
		expected_dir2 = {'file_b.txt': 1}
		self.assertEqual(expected_dir1, dict1_only)
		self.assertEqual(expected_dir2, dict2_only)

	def test_build_file_strings(self):
		# TODO: maybe add some string io testing
		file_count_dict_a = {'file_a.txt': 1, 'file_c.txt': 2}
		file_count_dict_b = {'file_a.txt': 3, 'file_b.txt': 1, 'file_d.txt': 1}
		dict1_only, dict2_only = get_dict_differences(file_count_dict_a, file_count_dict_b)
		build_file_strings(dict1_only, PRIMARY_DIRECTORY, SECONDARY_DIRECTORY)
		build_file_strings(dict2_only, SECONDARY_DIRECTORY, PRIMARY_DIRECTORY)


if __name__ == '__main__':
	unittest.main()
