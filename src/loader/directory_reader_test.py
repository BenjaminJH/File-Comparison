import unittest
import os
import test
from directory_reader import DirectoryReader

test_module_path = os.path.dirname(test.__file__)
dir1 = os.path.join(test_module_path, "example_directories", "test_directory_a")


class TestFileReader(unittest.TestCase):

	def test_get_file_counter_dict(self):
		reader = DirectoryReader(dir1)
		paths = reader.get_file_counter_dict()
		self.assertEqual({'file_a.txt': 1, 'file_c.txt': 2, 'file_d.txt': 1}, paths)

	def test_get_highest(self):
		reader = DirectoryReader(dir1)
		file = reader.get_highest()
		self.assertEqual(('file_c.txt', 2), file)

	def test_get_file_path_list(self):
		reader = DirectoryReader(dir1)
		paths = [path.replace("\\", "/") for path in reader.get_file_path_list()]  # Accounting in case of windows
		self.assertEqual(
			['/file_a.txt', '/file_c.txt', '/subdirectory_depth1_1/file_c.txt',  '/subdirectory_depth1_1/file_d.txt'],
			paths
		)
