import re


class tmLinker:
    def __init__(self):
        print("tmLinker")

    def run(self, data):
        mapper = {}

        for tiddler in data:
            title = tiddler["title"]
            content = tiddler["content"]
            links = re.findall("(?<=\[\[)(.*?)(?=\]\])", content)
            mapper[title] = links

        for key in mapper:
            print(key + " " + str(mapper[key]))

        return mapper
