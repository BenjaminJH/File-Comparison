# File-Comparison
A project designed to allow you to select two directories and compare files in each. 
Future iterations should include a gui, individual differences, duplicate file identification, etc.

example run command from commandline:

`python src/cli/cli.py --dir1='C:/Users/MyDir/test_a' --dir2='E:/ExternalDrive/test_b' --search_type="path"`

`python src/cli/cli.py --dir1='C:/Users/MyDir/test_a' --dir2='E:/ExternalDrive/test_b' --search_type="count"`

## Flags

- `--dir1` str: The primary directory
- `--dir2` str: The secondary directory
- `--search_type` `[path|count]`: The path compares full paths where-as count compares the filename occurance count

**NOTE:** End folders do not need the same name. Though you should be comparing folders with matching content.


# PROGRESS LISTING

This project currently provides a cli which handles some of the following:

- File path comparison between two directories
- Exact file name occurrence count comparing two directories
- Duplicate identification

Todo:
1. GUI:
	a. for selecting directories
	b. allowing you to open duplicates where mismatches occur (dependent on 1.)
2. Duplicate file comparison based on contents (e.g. one file might be more up to date)
3. Edit date comparison.
4. Turn off certain files/folders and keep track of this such that it wont be included in the comparison. (for example an external hdd may not want installer exes)
