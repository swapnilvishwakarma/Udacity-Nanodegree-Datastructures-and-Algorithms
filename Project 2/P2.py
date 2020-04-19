import os


def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.
    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.
    There are no limit to the depth of the subdirectories can be.
    Args:
    suffix(str): suffix if the file name to be found
    path(str): path of the file system
    Returns:
    a list of paths
    """
    try:
        PathList = os.listdir(path)
        FinalPath = []
        for item in PathList:
            item_path = os.path.join(path, item)
            if os.path.isdir(item_path):
                FinalPath += find_files(suffix, item_path)
            if os.path.isfile(item_path) and item_path.endswith(suffix):
                FinalPath.append(item_path)
        return FinalPath
    except:
        os.path.isdir(path)
        return 'Invalid Directory'


# Default test

print("Test 1")
print(find_files('.c', './testdir'))

print("Test 2")
print(find_files('', './testdir'))

print("Test 3")
print(find_files('.c', './testdir'))

# Non existent directory
print("Test 4")
print(find_files('.c', './asdf'))

# Empty Directory
print("Test 5")
print(find_files('.c', './emptydir'))
