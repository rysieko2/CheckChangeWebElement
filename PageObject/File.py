class File(object):
    def __init__(self, path):
        self.path = path

    def create_add_string_begin(self, string):
        file = open(self.path, 'w')
        file.write(string+"\n")
        file.close()

    def add_string_to_next_line(self, string):
        file = open(self.path, "a+")
        file.write(string+"\n")
        file.close()
