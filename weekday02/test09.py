def printable(cls):
    def _print(self):
        print(self.content,'装饰器')
    cls.print = _print
    return cls

class Document:
    def __init__(self,content):
        self.content = content
class Word(Document):pass
class Pdf(Document):pass

@printable
class PrintableWord(Word):pass # PrintableWord = printable(PrintableWord)
print(PrintableWord.__dict__)
print(PrintableWord.mro())

pw = PrintableWord('test string')
pw.print()

@printable
class PrintablePdf(Word):pass

pdf = PrintablePdf('PDF')
pdf.print()