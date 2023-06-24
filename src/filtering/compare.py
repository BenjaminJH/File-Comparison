from .collection_tools import get_list_differences, get_dict_differences, get_dict_intersecting_keys
from src.loader.filereader import get_file_path_list, get_file_counter_dict

LONG_BREAK = "-"*50
PRIMARY_DIRECTORY = "Primary Directory"
SECONDARY_DIRECTORY = "Secondary Directory"


def compare_by_file_path(dir1, dir2):
	"""
	Print the output for comparing filepaths between two directories

	:param dir1: first directory to check with
	:param dir2: secondary directory to check with
	:return:
	"""
	directory_a = get_file_path_list(dir1)
	directory_b = get_file_path_list(dir2)

	dir1_only, dir2_only = get_list_differences(directory_a, directory_b)

	print("#COMPARISON BY FILE PATH#")

	# Get files in Primary Directory that are not in the Secondary Directory
	build_file_strings(dir1_only, PRIMARY_DIRECTORY, SECONDARY_DIRECTORY)

	# Get files in Secondary Directory that are not in Primary Directory
	build_file_strings(dir2_only, SECONDARY_DIRECTORY, PRIMARY_DIRECTORY)

	return dir1_only, dir2_only


def compare_by_file_count(dir1, dir2):
	"""
	Print the output for comparing file occurrence count

	:param dir1: Primary directory path string
	:param dir2: Secondary directory path string
	:return:
	"""
	directory_a = get_file_counter_dict(dir1)[0]
	directory_b = get_file_counter_dict(dir2)[0]
	dict1_only, dict2_only = get_dict_differences(directory_a, directory_b)
	diff_count = 0

	print("#COMPARISON BY FILE COUNT#")

	# Get files in primary directory that are not in the secondary directory
	build_file_strings(dict1_only, PRIMARY_DIRECTORY, SECONDARY_DIRECTORY)

	# Get files in secondary directory that are not in primary directory
	build_file_strings(dict2_only, SECONDARY_DIRECTORY, PRIMARY_DIRECTORY)

	# Get file count differences
	print("\nMatching file quantity differences")
	print(LONG_BREAK)
	intersecting_keys = get_dict_intersecting_keys(directory_a, directory_b)
	for key in intersecting_keys:
		print("\"%s\" : Primary Directory has %s, Secondary Directory has %s" % (key, directory_a[key], directory_b[key]))
		diff_count += 1
	print(LONG_BREAK)
	print("%s of certain filename that dont line up" % diff_count)

	return dict1_only, dict2_only


def build_file_strings(dir, dir1_str, dir2_str):
	"""
	A set of print statements that get outputted to provide the user information on file mismatches

	:param dir: a collection containing filepaths either as values or keys
	:param dir1_str: [Primary Directory|Secondary Directory]
	:param dir2_str: [Secondary Directory|Primary Directory]
	:return:
	"""
	print(f"\nFiles in {dir1_str}, but in {dir2_str}")
	print(LONG_BREAK)
	for file in dir:
		print(f"{dir1_str} has \"%s\", {dir2_str} does not have this" % file)
	print(LONG_BREAK)
	print(len(dir), f"exist in the {dir1_str}, but not in the {dir2_str}.")
