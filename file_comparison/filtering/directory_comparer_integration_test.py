import pytest
import os
import test
from src.filtering.collection_tools import get_dict_differences
from src.filtering.directory_comparer import DirectoryComparer

path = os.path.dirname(test.__file__)
dir1 = os.path.join(path, "example_directories", "test_directory_a")
dir2 = os.path.join(path, "example_directories", "test_directory_b")


@pytest.mark.integration
def test_compare_by_file_path():
	built_str = DirectoryComparer(dir1, dir2).compare_by_file_path()\
		.replace("\\", "/")  # Accounting in case of windows
	expected_str = """#COMPARISON BY FILE PATH#
		
		Files in Primary Directory, but in Secondary Directory
		--------------------------------------------------
		/file_c.txt
		/subdirectory_depth1_1/file_c.txt
		/subdirectory_depth1_1/file_d.txt
		--------------------------------------------------
		3 exist in the Primary Directory, but not in the Secondary Directory.
		
		Files in Secondary Directory, but in Primary Directory
		--------------------------------------------------
		/file_b.txt
		/subdirectory_depth1_1/file_a.txt
		/subdirectory_depth1_1/subdirectory_depth2_1/file_a.txt
		/subdirectory_depth1_1/subdirectory_depth2_1/file_d.txt
		--------------------------------------------------
		4 exist in the Secondary Directory, but not in the Primary Directory.""".replace("\t", "")
	assert expected_str == built_str

@pytest.mark.integration
def test_compare_by_file_count():
	built_str = DirectoryComparer(dir1, dir2).compare_by_file_count()
	expected_str = """#COMPARISON BY FILE COUNT#
		
		Files in Primary Directory, but in Secondary Directory
		--------------------------------------------------
		file_c.txt
		--------------------------------------------------
		1 exist in the Primary Directory, but not in the Secondary Directory.
		
		Files in Secondary Directory, but in Primary Directory
		--------------------------------------------------
		file_b.txt
		--------------------------------------------------
		1 exist in the Secondary Directory, but not in the Primary Directory.
		
		Matching file quantity differences
		--------------------------------------------------
		file_a.txt: Primary Directory has 1, Secondary Directory has 3
		--------------------------------------------------
		1 of certain filename that dont line up""".replace("\t", "")
	assert expected_str == built_str
