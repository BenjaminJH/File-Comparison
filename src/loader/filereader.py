import os


def drive_string_index(drive_string):
	# TODO: to be deprecated
	# If found return next index past it so it's cut out of the comparison string, otherwise assume it isn't present.
	idx = drive_string.find(':\\')
	if idx >= 0:
		return idx + 2
	return 0


def strip_drive_string(directory):
	# TODO: apply this, replacing locations where drive_string_index was used
	"""
	Provided a directory, remove the drive string at the front
	:param directory: a directory path (e.g. "C:\\Users\\MyUser")
	:return: the directory passed in without a drive if one is present
	"""
	split_directory = directory.split(':\\')
	if len(split_directory) == 1:
		return directory
	elif len(split_directory) == 2:
		return split_directory[1]
	raise ValueError("Directory must be a non-empty string and cannot contain more than one drive string.")


def get_file_counter_dict(directory):
	"""
	Walk through directory and count the number of occurrences of of certain file counts
	:param directory: a directory path (e.g. "C:\\Users\\MyUser")
	:return: a dictionary counting the instances of certain files
	"""
	# Get a dict of filenames with a counter (example file found {"Song1.mp3": 5})
	counter_dict = {}
	for root, dirs, files in os.walk(directory):
		for file in files:
			# Counter for exact filename match. No longer needed, we could use a list.
			counter_dict[file] = counter_dict.get(file, 0) + 1

	# Commented out snippet used to find the most excessively large amount of dupes, could become relevant later on.
	highest = ("", 0)
	for key in counter_dict.keys():
		if counter_dict[key] > highest[1]:
			highest = (key, counter_dict[key])
	return counter_dict, highest


def get_file_path_list(directory):
	# TODO: clean this method up
	"""
	Walk through directory and get a list of file paths (example file found "C:\\Users\\MyUser\\Music\\Song1.mp3")
	:param directory: a directory path (e.g. "C:\\Users\\MyUser")
	:return: a list of filepaths (e.g. ["C:\\Users\\MyUser\\Music\\Song1.mp3", "C:\\Users\\MyUser\\Desktop\\me.py"]
	"""
	full_path_files = []
	# r=root, d=directories, f = files
	for root, dirs, files in os.walk(directory):
		for file in files:
			drive_slash = drive_string_index(directory)	 # Index just past drive (e.g. 0 if none is present, 3 for "C:\")
			driveless_header_directory = directory[drive_slash:]  # We use this for removing header folders. Strip drive (e.g. "\Users\MyUser\Music\")

			file_path = os.path.join(root, file)  # File path (e.g. "test_directory_a\file_a.txt" or  "C:\Users\MyUser\Music\Album\Song1.mp3")
			driveless_path = file_path[drive_slash:]  # Path without the drive (e.g. "Users\MyUser\Music\Album\Song1.mp3")
			severed_path = driveless_path.replace(driveless_header_directory, "")  # Path without drive or header folders (e.g. "\Album\Song1.mp3")

			full_path_files.append(severed_path)
	return full_path_files
