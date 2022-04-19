import os

def get_file_dict(directory):
    # Getting the current work directory (cwd)
    thisdir = directory

    g = {}
    # r=root, d=directories, f = files
    for r, d, f in os.walk(thisdir):
        for file in f:
            #print(os.path.join(r, file))
            if file not in g.keys():
                g[file] = 0
            g[file] += 1
    '''
    prev_highest = ("", 0)
    for key in g.keys():
        if g[key] > prev_highest[1]:
            prev_highest = (key, g[key])
    '''
    return g

def anotb(dict1, dict2, label1, label2):
    not_in_d2 = 0
    in_d2_but_differing_amounts = 0
    for new_key in dict1.keys():
        #Exists in a but not b, or a has a different amount than b
        if (new_key not in dict2):
            message = "%s has \"%s\" %s Does not have this" % (label1, new_key, label2)
            print(message)
            not_in_d2 += 1
            continue
        if (dict1[new_key] != dict2[new_key]):
            message = "\"%s\" : %s has %s, %s has %s" % (new_key, label1, dict1[new_key], label2, dict2[new_key])
            print(message)
            in_d2_but_differing_amounts += 1
            continue
    return not_in_d2, in_d2_but_differing_amounts

dir1=r"E:\1. Laptop\Windows(Partition4)\Music"
dir2=r"C:\Users\Ben\Music"

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
