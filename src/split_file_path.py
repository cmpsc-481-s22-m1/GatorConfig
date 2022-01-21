"""Split file path module."""
def split_file_path(paths):
    """Separates directories from files paths and stores them as dictionaries inside a dictionary."""
    output = {}
    for key, value in paths.items():
        directories = key.split('/')
        dir_dic = output
        for direc in directories[:-1]:
            if direc not in dir_dic:
                dir_dic[direc] = {}
            dir_dic = dir_dic[direc]
        dir_dic[directories[-1]] = value

    return output

# example dictionary containing three file paths
path_dic = {
    'src/main/java/samplelab/SampleLabMain.java': [''],
    'src/main/java/samplelab/DataClass.java': [''],
    'writing/reflection.md': ['']
}
final_dic = split_file_path(path_dic)
print(final_dic)
