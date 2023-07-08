import os


class DirectoryReader:
	directory = None  # A directory path (e.g. "C:/Users/MyUser")
	file_path_list = []  # A list of found file paths (e.g. ["C:/Users/MyUser/docs/file_a.txt"])
	file_counter_dict = {}  # A dictionary of found file counts (e.g. {'file_a.txt': 1, 'file_c.txt': 2})
	_highest_occurring_file = None  # A tuple of the file with the most dupes of that name in the file_counter_dict

	def __init__(self, directory):
		self.directory = directory

	def get_file_counter_dict(self, force_recalc=False):
		"""
		Walk through directory and count the number of occurrences of certain file counts
		:param force_recalc: recalculate even if field is already filled.
		:return: a dictionary counting the file count in a directory with filename as key and occurrences as the value
		"""
		if not (self.file_counter_dict or force_recalc):
			counter_dict = {}
			for root, dirs, files in os.walk(self.directory):
				for file in files:
					counter_dict[file] = counter_dict.get(file, 0) + 1
			self.file_counter_dict = counter_dict

		return self.file_counter_dict

	def get_highest(self, force_recalc=False):
		"""
		Get the file name and number of occurrences of the highest occurring filename for a directory
		:param force_recalc: recalculate even if field is already filled.
		:return: a tuple containing the name and count of the highest occurring file
		"""
		if not (self._highest_occurring_file or force_recalc):
			file_count = self.get_file_counter_dict()
			highest = ("", 0)
			for key, val in file_count.items():
				if val > highest[1]:
					highest = (key, val)
			self._highest_occurring_file = highest

		return self._highest_occurring_file

	def get_file_path_list(self, force_recalc=False):
		"""
		Walk through directory and get a list of relative file paths from the directory including nested subdirectories
		:param force_recalc: recalculate even if field is already filled.
		:return: a list of filepaths relative to the directory.
		"""
		if not (self.file_path_list or force_recalc):
			full_path_files = []
			# r=root, d=directories, f = files
			for root, _, files in os.walk(self.directory):
				for file in files:
					full_system_file_path = os.path.join(root, file)
					relative_path = full_system_file_path.replace(self.directory, "")
					full_path_files.append(relative_path)
			self.file_path_list = full_path_files

		return self.file_path_list
