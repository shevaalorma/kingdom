class Printable:
    def _print(self):
        print(self.content,'装饰器')

class Document:
    def __init__(self,content):
        self.content = content

class Word(Document):pass
class Pdf(Document):pass

class PrintableWord(Printable,Word):pass
print(PrintableWord.__dict__)
print(PrintableWord.mro())

pw = PrintableWord('test string')
pw._print()