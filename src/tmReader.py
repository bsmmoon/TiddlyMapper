

class tmReader:
    def __init__(self):
        print("tmReader")

    def run(self, fileDirectory):
        html = ""
        with open(fileDirectory, encoding="UTF8") as openfileobject:
            for line in openfileobject:
                html += line.strip()
        print(len(html))
        return html
