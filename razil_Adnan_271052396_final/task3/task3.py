#factory pattern
from abc import ABC,abstractmethod

class Document(ABC):
    @abstractmethod
    def open(self):
        pass
    @abstractmethod
    def read(self):
        pass
    @abstractmethod
    def save(self):
        pass


class PDF(Document):
    def __init__(self, fname, fsize, content):
        self.name = fname
        self.fsize = fsize
        self.content = content

    def open(self):
        print("opening a pdf file")

    def read(self):
        print("reading a pdf file")

    def save(self):
        print("saving a pdf file")


class Excel(Document):
    def __init__(self, fname, fsize, content):
        self.name = fname
        self.fsize = fsize
        self.content = content

    def open(self):
        print("opening a excel file")

    def read(self):
        print("reading a excel file")

    def save(self):
        print("saving a excel file")

class Word(Document):
    def __init__(self,fname,fsize,content):
        self.name=fname
        self.fsize=fsize
        self.content=content

    def open(self):
        print("opening a word file")

    def read(self):
        print("reading a word  file")

    def save(self):
        print("saving a word  file")


class DocumentFactory():
    def __init__(self,doctype,fname,fsize,content):
        self.doctype =doctype
        self.name = fname
        self.fsize = fsize
        self.content = content

        if self.doctype=="word":
            self.doctype=Word(fname,fsize,content)
            self.doctype.open()
            self.doctype.read()
            self.doctype.save()
        elif self.doctype=="pdf":
            self.doctype=PDF(fname,fsize,content)
            self.doctype.open()
            self.doctype.read()
            self.doctype.save()
        elif self.doctype=="excel":
            self.doctype =Excel(fname,fsize,content)
            self.doctype.open()
            self.doctype.read()
            self.doctype.save()


def __main__():
    doctype= input("enter document type")
    fname= input("enter name")
    fsize=input("enter size")
    content= input("enter content")
    factory = DocumentFactory(doctype,fname,fsize,content)


__main__()
