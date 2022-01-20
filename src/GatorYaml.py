class GatorYaml:
    def __init__(self):
        self.spaces = 4
        self.tabs = 0
        self.output = ""
        self.keywords = ["(pure)"]

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
            if isinstance(d[k], list):
                self.output_key(k)
                self.enum_list(d[k])
            elif isinstance(d[k], dict):
                self.output_key(k)
                self.enum_dict(d[k])
            else:
                if not self.is_keyword(k, d[k]):
                    self.output_key_value(k, d[k])

        self.tabs -= 1

    def output_list_item(self, item):
        self.output += (" "*self.spaces)*self.tabs + " -" + item + "\n"

    def output_key(self, key):
        self.output += (" "*self.spaces)*self.tabs + key + ":\n"

    def output_key_value(self, key, value):
        self.output += ((" "*self.spaces)*self.tabs) + key + ": " + value + "\n"

    def is_keyword(self, key, value):
        if key in self.keywords:
            self.output += (" "*self.spaces)*self.tabs + key + " " + value + "\n"
            return True
        return False

# d = {"test":"Bing bong", "test2":["bing", "bong"], "test3":{"Indent!":"wooooo!", "wanna see me do it again?":{"Bada-bing": "bada-boom!", "list?":["Hello", "Steve"]}}, "test4":"Continue?", "(pure)":"Very pure text here."}
#
# yaml = GatorYaml()
# print(yaml.dump(d))
