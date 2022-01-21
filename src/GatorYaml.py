from src.split_file_path import split_file_path

class GatorYaml:
    def __init__(self, indent=4, spaces=4):
        self.spaces = spaces
        self.tabs = -1
        self.output = ""
        self.keywords = ["(pure)"]
        self.indents = indent

    def dump(self, dic):

        self.enum_dict(dic)

        return self.output

    def enum_list(self, l):
        for i in l:
            if isinstance(i, dict):
                self.tabs += 1
                self.enum_dict(i)
            else:
                self.output_list_item(i)

    def enum_dict(self, d):
        self.tabs += 1

        for k in d.keys():
            if k == "indent":
                self.indents = int(d[k])

            if k == "files":
                # if isinstance(d[k], list):
                #     self.enum_list(d[k])
                if isinstance(d[k], dict):
                    self.enum_file_dict(d[k])
                    pass
            elif isinstance(d[k], list):
                self.output_key(k)
                self.enum_list(d[k])
            elif isinstance(d[k], dict):
                self.output_key(k)
                self.enum_dict(d[k])
            else:
                if not self.is_keyword(k, d[k]):
                    self.output_key_value(k, d[k])

        self.tabs -= 1

    def enum_file_dict(self, files):
        self.tabs += 1

        for k in files:
            if isinstance(files[k], dict):
                self.output_key(k)
                self.enum_file_dict(files[k])
            elif isinstance(files[k], list):
                self.output_key(k)
                self.enum_file_list(files[k])

        self.tabs -= 1

    def enum_file_list(self, list):
        for item in list:
            self.output += (" "*self.spaces)*self.indents + str(item) + "\n"

    def output_list_item(self, item):
        self.output += (" "*self.spaces)*self.tabs + " -" + str(item) + "\n"

    def output_key(self, key):
        self.output += (" "*self.spaces)*self.tabs + str(key) + ":\n"

    def output_key_value(self, key, value):
        self.output += ((" "*self.spaces)*self.tabs) + str(key) + ": " + str(value) + "\n"

    def is_keyword(self, key, value):
        if key in self.keywords:
            self.output += (" "*self.spaces)*self.tabs + str(key) + " " + str(value) + "\n"
            return True
        return False



# d = {"test":"Bing bong", "test2":["bing", "bong"], "test3":{"Indent!":"wooooo!", "wanna see me do it again?":{"Bada-bing": "bada-boom!", "list?":["Hello", "Steve"]}}, "test4":"Continue?", "(pure)":"Very pure text here.", }

# test = {
#     "name": "gatorgrader-samplelab",
#     "break": True,
#     "fastfail": False,
#     "indent": 4,
#     "idcommand": "echo $TRAVIS_REPO_SLUG",
#     "version": "v0.2.0",
#     "executables": ["cat", "bash"],
#     "startup": "./config/startup.sh",
#     "reflection": "writing/reflection.md",
#     "files": split_file_path({"src/main/java/test.java":
#                              ["--exists", "--single 1 --language Java",
#                               "--multi 3 --language Java",
#                               "--fragment \"println(\" --count 2",
#                               "--fragment \"new DataClass(\" --count 1",
#                               "--regex \"new\s+\S+?\(.*?\)\" --count 2 --exact"],
#                               "src/main/java/test2.java":
#                               ["--exists", "--multi 1 --language Java",
#                                "--single 1 --language Java",
#                                "--fragment \"int \" --count 1"
#                                ]})
# }
# # combo = test | )
#
#
# yaml = GatorYaml()
#
# f = open("./test.yml", "w+")
#
# f.write(yaml.dump(test))
