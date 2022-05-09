# File-Comparison
A project designed to allow you to select two directories and compare files in each. Future iterations should include a gui, individual differences, duplicate file identification, etc.

example run command from commandline:

python -c 'from compare_directory_content import run_comparison; run_comparison()' --dir1="C:\Users\Ben\test_a\" --dir2="E:\ExternalDrive\test_b\"

NOTE: End folders do not need the same name. Though you should be comparing folders with matching content.