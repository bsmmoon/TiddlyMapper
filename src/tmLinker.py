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
            links = list(map(self.getRealLink, links))
            mapper[title] = links

        return mapper

    def getRealLink(self, link):
        link = link.split("|")
        if len(link) > 1:
            return link[1]
        else:
            return link[0]
