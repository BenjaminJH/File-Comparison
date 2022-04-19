import os

"""
This is the foundation for a file comparison software, future versions will likely scrap existing code and add far more.
Currently does:
- compare exact filename matches and tally after traversing every file in a directory.
- duplicate identification

Todo:
1. compare from certain path downwards rather than just filename (i.e. may exist in other sub-directories)
2. GUI:
    a. for selecting directories
    b. allowing you to open duplicates where mismatches occur (dependent on 1.)
3. Duplicate file comparison based on contents (e.g. one file might be more up to date)
4. Edit date comparison.
5. Unit testing
"""

def get_file_dict(directory):
    # Getting the current work directory (cwd)
    thisdir = directory

    g = {}
    # r=root, d=directories, f = files
    for r, d, f in os.walk(thisdir):
        for file in f:
            #print(os.path.join(r, file))
            #Counter for exact filename match. This should be changed at a later point to look at the matching directory header (e.g. /music/)
            g[file] = g.get(file, 0) + 1
    ''' #Commented out snippet used to find the most excessively large amount of dupes, could become relevant later on.
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

dir1=r'test_directory_a'
dir2=r'test_directory_b'

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
