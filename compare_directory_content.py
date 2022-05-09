import os
import argparse

"""
This is the foundation for a file comparison software, future versions will likely scrap existing code and add far more.
Currently does:
- compare exact filename matches and tally after traversing every file in a directory. (might not tally anymore with directory change)
- duplicate identification

Todo:
1. GUI:
	a. for selecting directories
	b. allowing you to open duplicates where mismatches occur (dependent on 1.)
2. Duplicate file comparison based on contents (e.g. one file might be more up to date)
3. Edit date comparison.
4. Unit testing
5. Turn off certain files/folders and keep track of this such that it wont be included in the comparison. (for example an external hdd may not want installer exes)
"""

def drive_string_index(drive_string):
	# If found return next index past it so it's cut out of the comparison string, otherwise assume it isn't present.
	idx = drive_string.find(':\\')
	if idx >= 0:
		return idx + 2
	return 0

def get_file_dict(directory):
	#Get a list/dict of file paths (example file found "C:\Users\Ben\Music\Album\Song1.mp3")
	thisdir = directory		# Getting the current work directory (cwd)
	g = {}
	# r=root, d=directories, f = files
	for root, dirs, files in os.walk(thisdir):	# Walk through current or full directory (e.g. "test_directory_a\" or "C:\Users\Ben\Music\")
		for file in files:
			#print(root, dirs, files)
			drive_slash = drive_string_index(thisdir)	# Index just past drive (e.g. 0 if none is present, 3 for "C:\")
			driveless_header_directory = thisdir[drive_slash:]	# We use this for removing header folders. Strip drive (e.g. "\Users\Ben\Music\")

			file_path = os.path.join(root, file)	# File path (e.g. "test_directory_a\file_a.txt" or  "C:\Users\Ben\Music\Album\Song1.mp3")
			driveless_path = file_path[drive_slash:]	# Path without the drive (e.g. "Users\Ben\Music\Album\Song1.mp3")
			severed_path = driveless_path.replace(driveless_header_directory, "")	# Path without drive or header folders (e.g. "\Album\Song1.mp3")

			g[severed_path] = g.get(severed_path, 0) + 1 # Counter for exact filename match. No longer needed, we could use a list.
	''' # Commented out snippet used to find the most excessively large amount of dupes, could become relevant later on.
	prev_highest = ("", 0)
	for key in g.keys():
		if g[key] > prev_highest[1]:
			prev_highest = (key, g[key])
	'''
	return g

def anotb(dict1, dict2, directory_1_label, directory_2_label):
	not_in_d2 = 0
	in_d2_but_differing_amounts = 0
	for new_key in dict1.keys():
		#Exists in a but not b, or a has a different amount than b
		if (new_key not in dict2):
			message = "%s has \"%s\" %s Does not have this" % (directory_1_label, new_key, directory_2_label)
			print(message)
			not_in_d2 += 1
			continue
		if (dict1[new_key] != dict2[new_key]):
			message = "\"%s\" : %s has %s, %s has %s" % (new_key, directory_1_label, dict1[new_key], directory_2_label, dict2[new_key])
			print(message)
			in_d2_but_differing_amounts += 1
			continue
	return not_in_d2, in_d2_but_differing_amounts

parser = argparse.ArgumentParser(description='Directory paths')
parser.add_argument("--dir1", type=str, default=r'test_directory_a')
parser.add_argument("--dir2", type=str, default=r'test_directory_b')
args = parser.parse_args()
dir1 = args.dir1
dir2 = args.dir2
#print(dir1)
#print(dir2)

directory_a = get_file_dict(dir1)
directory_b = get_file_dict(dir2)
long_break = "-"*50
#Get files in primary directory that are not in the secondary directory
print("\nFiles in primary directory, not in secondary directory b\n"+long_break)
primary_directory = anotb(directory_a, directory_b, "Primary Directory", "Secondary Directory")
print(long_break)
print(primary_directory[0], "exist in primary directory, but not in the secondary one", \
		primary_directory[1], "amounts of certain filename that dont line up\n")

#Get files in secondary directory that are not in primary directory
print("\nFiles in secondary directory but not in primary directory\n"+long_break)
secondary_directory = anotb(directory_b, directory_a, "Secondary Directory", "Primary Directory")
print(long_break)
print(secondary_directory[0], "exist in secondary directory, but not in the primary one", \
		secondary_directory[1], "amounts of certain filename that dont line up") 
