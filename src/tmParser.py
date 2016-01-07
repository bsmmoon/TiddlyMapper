

class tmParser:
    def __init__(self):
        print("tmParser")

    def run(self, html):
        result = ""
        return result

    def find(self, text, front, back):
        startIdx = text.find(front) + len(front)
        offset = text[startIdx:].find(back)
        endIdx = startIdx + offset
        return text[startIdx:endIdx]
