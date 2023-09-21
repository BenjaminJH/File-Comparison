# TODO:

1. Feature: Add a GUI:
	a. for selecting directories
	b. allowing you to open duplicates where mismatches occur (dependent on 1.)
2. Duplicate file comparison based on contents (e.g. one file might be more up to date)
3. Edit date comparison.
4. Turn off certain files/folders and keep track of this such that it won't be included in the comparison. (for example an external hdd may not want installer exes)
5. Make the output strings into an object containing a header, a set of contents, footer, etc. This way we can pass objects back and forth far more securely and just use a .String() method or something for the output.
6. Variation that just returns everything in one directory for both file path and file count, this way people could check if anything seemed out of place, more useful for file count.
7. Make dockerfile with helm charts, spin up docker file, local mount test files and then integration test it works

