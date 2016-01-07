import re


class tmParser:
    def __init__(self):
        print("tmParser")

    def run(self, html):
        print(len(html))
        html = self.find(html, "<div created=", "Library modules ~~-->")
        print(len(html))
        tiddlers = re.findall("<div created=(.*?)</pre", html)

        for i in range(len(tiddlers)):
            tiddler = tiddlers[i]
            objTiddler = {}
            objTiddler["created"] = self.search("(?<=\")(.*?)(?=\")", tiddler)
            objTiddler["modified"] = self.search("(?<=modified=\")(.*?)(?=\")", tiddler)
            objTiddler["tags"] = self.search("(?<=tags=\")(.*?)(?=\")", tiddler)
            objTiddler["title"] = self.search("(?<=title=\")(.*?)(?=\")", tiddler)
            objTiddler["content"] = self.search("(?<=<pre>)(.*?)(?=$)", tiddler)
            tiddlers[i] = objTiddler

        for tiddler in tiddlers:
            print(tiddler)
        print("")

        return tiddlers

    def search(self, regex, text):
        result = re.search(regex, text)
        if result is None:
            return ""
        else:
            return result.group(0)

    def find(self, text, front, back):
        startIdx = text.find(front)
        offset = text[startIdx:].find(back)
        endIdx = startIdx + offset
        return text[startIdx:endIdx]
