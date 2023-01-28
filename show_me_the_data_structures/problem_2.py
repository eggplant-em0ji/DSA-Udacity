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
    if os.path.exists(path):
        files = []
        # O(1); only 1 path provided
        folders_to_search = [path]
        while folders_to_search:
            current_folder = folders_to_search.pop(0) + "/"
            items_in_current_folder = os.listdir(current_folder)
            # O(n) for n items in a folder, which accomplishes both searching for files with the provided suffix and adding newly found folders to the folders_to_search list
            for item in items_in_current_folder:
                item_path = current_folder + item
                # O(n) for n items in a new folder each time folders_to_search adds a new folder
                if os.path.isdir(item_path):
                    folders_to_search.append(item_path)
                elif str(item_path).endswith(suffix):
                    files.append(item_path)
        return files
    else:
        return None

# Add your own test cases: include at least three test cases
# and two of them must include edge cases, such as null, empty or very large values

# Test Case 1: Finding files ending with ".c"
print(f'Test Case 1: find_files(".c", "testdir") should return a list of 4 item paths ending in ".c" and returns {find_files(".c", "testdir")}\n')

# Test Case 2: Empty suffix and path
try:
    find_files()
except TypeError:
    print('Test Case 2: find_files() results in a TypeError because no path was given\n')

# Test Case 3: None as path
try:
    find_files(".c", None)
except TypeError:
    print('Test Case 3: find_files(None) results in a TypeError because None is not a valid path in the function os.path.exists(path)\n')

# Test Case 4: Empty string as path
print(f'Test Case 4: find_files(".c", "") should return None and does return {find_files(".c", "")} because an empty string was passed as the path to search\n')