class Dictionary:
    def __init__(self):
        self._dict = []

    def loadDictionary(self,path):
        f=open(path, "r")
        righe=f.readlines()
        for riga in righe:
            self._dict.append(riga)

    def printAll(self):
        for p in self._dict:
            print(p)

    @property
    def dict(self):
        return self._dict