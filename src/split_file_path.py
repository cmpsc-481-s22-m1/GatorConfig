# separates directories from files paths and stores them as dictionaries inside a dictionary
def split_file_path(path_list):
    output = {}
    for path in path_list:
        directories = path.split('/')
        dir_dic = output
        for direc in directories[:-1]:
            # direc = direc + "/" # adds / to end of dir
            if direc not in dir_dic:
                dir_dic[direc] = {}
            dir_dic = dir_dic[direc]
        dir_dic[directories[-1]] = ['']

    return output

# example dictionary containing three file paths
path_list = [
    'src/main/java/samplelab/SampleLabMain.java', 
    'src/main/java/samplelab/DataClass.java',
    'writing/reflection.md'
]
final_dic = split_file_path(path_list)
print(final_dic)
# {'src': {'main': {'java': {'samplelab': {'SampleLabMain.java': [''], 'DataClass.java': ['']}}}}, 'writing': {'reflection.md': ['']}}
