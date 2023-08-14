from .collection_tools import get_list_differences, get_dict_differences, get_dict_where_value_differs
from file_comparison.loader.directory_reader import DirectoryReader

LONG_BREAK = "-"*50


class DirectoryComparer:
	PRIMARY_DIRECTORY = "Primary Directory"
	SECONDARY_DIRECTORY = "Secondary Directory"
	directory_readers = []  # A list of directory readers, for now we're putting it in a list, making it extensible

	def __init__(self, dir1, dir2):
		for directory in [dir1, dir2]:
			self.directory_readers.append(DirectoryReader(directory))

	def compare_by_file_path(self):
		"""
		Print the output for comparing filepaths between two directories
		:return directory_a_only: a list of file paths that only exist in directory 1
		:return directory_b_only: a list of file paths that only exist in directory 2
		"""
		directory_a = self.directory_readers[0].get_file_path_list()
		directory_b = self.directory_readers[1].get_file_path_list()
		directory_a_only, directory_b_only = get_list_differences(directory_a, directory_b)

		# Output built strings together
		header = "#COMPARISON BY FILE PATH#"
		directory_a_only_str = self.build_file_strings(directory_a_only, self.PRIMARY_DIRECTORY, self.SECONDARY_DIRECTORY)
		directory_b_only_str = self.build_file_strings(directory_b_only, self.SECONDARY_DIRECTORY, self.PRIMARY_DIRECTORY)
		built_str = "\n".join([header, directory_a_only_str, directory_b_only_str])

		return built_str

	def compare_by_file_count(self):
		"""
		Print the output for comparing file occurrence count
		:return directory_a_only: a dict of file names that only exist in directory 1
		:return directory_b_only: a dict of file names that only exist in directory 2
		"""
		directory_a = self.directory_readers[0].get_file_counter_dict()
		directory_b = self.directory_readers[1].get_file_counter_dict()
		directory_a_only, directory_b_only = get_dict_differences(directory_a, directory_b)

		# Output built strings together
		header = "#COMPARISON BY FILE COUNT#"
		directory_a_only_str = self.build_file_strings(directory_a_only, self.PRIMARY_DIRECTORY, self.SECONDARY_DIRECTORY)
		directory_b_only_str = self.build_file_strings(directory_b_only, self.SECONDARY_DIRECTORY, self.PRIMARY_DIRECTORY)
		diff_str = self.build_file_count_differences_strings(directory_a, directory_b)
		built_str = "\n".join([header, directory_a_only_str, directory_b_only_str, diff_str])

		return built_str

	@staticmethod
	def build_file_strings(unique_to_dir_a, dir_a_str, dir_b_str):
		"""
		Build a string that provide the user information on file mismatches

		:param unique_to_dir_a: a collection containing filepaths either as values or keys only in dir_a
		:param dir_a_str: [Primary Directory|Secondary Directory]
		:param dir_b_str: [Secondary Directory|Primary Directory]
		:return built_string: output strings from comparing 2 directories
		"""
		header = f"\nFiles in {dir_a_str}, but not in {dir_b_str}"
		footer = f"{len(unique_to_dir_a)} exist in the {dir_a_str}, but not in the {dir_b_str}."
		built_string = "\n".join([header, LONG_BREAK, "\n".join(sorted(unique_to_dir_a)), LONG_BREAK, footer])

		return built_string

	@staticmethod
	def build_file_count_differences_strings(filecount_dict_a, filecount_dict_b):
		"""
		Build a string that provide the user information on file count mismatches

		:param filecount_dict_a: first dict containing count of occurrences in a (sub)directory of a given filename
		:param filecount_dict_b: second dict containing count of occurrences in a (sub)directory of a given filename
		:return built_string: output strings of differences between the provided filecount dictionaries
		"""
		header = "\nMatching file quantity differences"
		differing_values_for_key_matches = get_dict_where_value_differs(filecount_dict_a, filecount_dict_b)
		mismatches = [
			f"{key}: Primary Directory has {filecount_dict_a[key]}, Secondary Directory has {filecount_dict_b[key]}"
			for key in differing_values_for_key_matches
		]
		diff_count_str = f"{len(mismatches)} of certain filename that dont line up"
		built_string = "\n".join([header, LONG_BREAK, "\n".join(mismatches), LONG_BREAK, diff_count_str])

		return built_string
