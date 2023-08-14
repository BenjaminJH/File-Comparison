import unittest
from file_comparison.filtering.collection_tools import get_dict_differences
from file_comparison.filtering.directory_comparer import DirectoryComparer


class TestDirectoryComparer(unittest.TestCase):

	def test_build_file_strings(self):
		file_count_dict_a = {'file_a.txt': 1, 'file_c.txt': 2}
		file_count_dict_b = {'file_a.txt': 3, 'file_b.txt': 1, 'file_d.txt': 1}
		dict1_only, dict2_only = get_dict_differences(file_count_dict_a, file_count_dict_b)
		expected_directory_a_str = """
			Files in Primary Directory, but not in Secondary Directory
			--------------------------------------------------
			file_c.txt
			--------------------------------------------------
			1 exist in the Primary Directory, but not in the Secondary Directory.""".replace("\t", "")
		expected_directory_b_str = """
			Files in Primary Directory, but not in Secondary Directory
			--------------------------------------------------
			file_b.txt
			file_d.txt
			--------------------------------------------------
			2 exist in the Primary Directory, but not in the Secondary Directory.""".replace("\t", "")
		directory_a_only_str = DirectoryComparer.build_file_strings(
			dict1_only,
			DirectoryComparer.PRIMARY_DIRECTORY,
			DirectoryComparer.SECONDARY_DIRECTORY
		)
		directory_b_only_str = DirectoryComparer.build_file_strings(
			dict2_only,
			DirectoryComparer.PRIMARY_DIRECTORY,
			DirectoryComparer.SECONDARY_DIRECTORY
		)
		self.assertEqual(expected_directory_a_str, directory_a_only_str)
		self.assertEqual(expected_directory_b_str, directory_b_only_str)

	def test_build_file_count_differences_strings(self):
		file_count_dict_a = {'file_a.txt': 1, 'file_c.txt': 2}
		file_count_dict_b = {'file_a.txt': 3, 'file_b.txt': 1, 'file_d.txt': 1}
		expected_diff_str = """
			Matching file quantity differences
			--------------------------------------------------
			file_a.txt: Primary Directory has 1, Secondary Directory has 3
			--------------------------------------------------
			1 of certain filename that dont line up""".replace("\t", "")
		diff_str = DirectoryComparer.build_file_count_differences_strings(file_count_dict_a, file_count_dict_b)
		self.assertEqual(expected_diff_str, diff_str)


if __name__ == '__main__':
	unittest.main()
