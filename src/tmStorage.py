import os


class tmStorage:
    def __init__(self):
        print("tmStorage")
        self.dataDir = "./data"
        self.fileName = "/result.csv"
        self.fileDirectory = self.dataDir + self.fileName
        self.writeData(self.fileDirectory, "")

    def run(self, data):
        for key in data:
            print(key + " " + str(data[key]))

        self.ensure_dir(self.dataDir)
        self.ensure_file(self.fileDirectory)
        for key in data:
            line = key + ";" + ';'.join(data[key]) + "\n"
            self.appendData(self.fileDirectory, line)

    def ensure_file(self, fileDirectory):
        if not os.path.isfile(fileDirectory):
            self.writeData(fileDirectory, "")

    def ensure_dir(self, directory):
        if not os.path.isdir(directory):
            os.makedirs(directory)
            return False
        else:
            return True

    def writeData(self, fileDirectory, text):
        with open(fileDirectory, 'w', encoding='UTF-8') as f:
            f.write(text)

    def appendData(self, fileDirectory, text):
        with open(fileDirectory, 'a', encoding='UTF-8') as f:
            f.write(text)
