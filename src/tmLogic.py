from tmReader import tmReader
from tmParser import tmParser
from tmStorage import tmStorage
from tmLinker import tmLinker


class tmLogic:
    def __init__(self):
        print("tmLogic")
        self.reader = tmReader()
        self.parser = tmParser()
        self.storage = tmStorage()
        self.linker = tmLinker()

    def run(self):
        fileDirectory = "./data/test.html"
        html = self.reader.run(fileDirectory)
        data = self.parser.run(html)
        data = self.linker.run(data)
        self.storage.run(data)
