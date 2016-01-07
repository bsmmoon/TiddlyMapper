from tmReader import tmReader
from tmParser import tmParser
from tmStorage import tmStorage


class tmLogic:
    def __init__(self):
        print("tmLogic")
        self.reader = tmReader()
        self.parser = tmParser()
        self.storage = tmStorage()

    def run(self):
        fileDirectory = "./data/test.html"
        html = self.reader.run(fileDirectory)
        data = self.parser.run(html)
        self.storage.run(data)
