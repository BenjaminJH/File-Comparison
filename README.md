# File-Comparison
A project designed to allow you to select two directories and compare files in each. 
Future iterations should include a gui, individual differences, duplicate file identification, etc.

example run command from commandline:

    python src/cli/cli.py --dir1='C:/Users/MyDir/test_a' --dir2='E:/ExternalDrive/test_b' --search_type="path"

## Flags

- `--dir1` str: The primary directory
- `--dir2` str: The secondary directory
- `--search_type` `[path|count]`: The path compares full paths where-as count compares the filename occurance count

**NOTE:** End folders do not need the same name. Though you should be comparing folders with matching content.

# Building and running

From the root of the project run the following to build the image:

    docker build -t file-comparison .

Run the image using the following, replace the flags with your relevant inputs:

    docker run file-comparison --dir1='C:/Users/MyDir/test_a' --dir2='E:/ExternalDrive/test_b' --search_type="path"

# PROGRESS LISTING

This project currently provides a cli which handles some of the following:

- File path comparison between two directories
- Exact file name occurrence count comparing two directories
- Duplicate identification
