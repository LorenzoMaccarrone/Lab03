import time

import multiDictionary as md

class SpellChecker:

    def __init__(self):
        pass

    def handleSentence(self, txtIn, language):
        txtInput=replaceChars(txtIn.lower())
        #dapprima salviamoci le parole in un vettore in modo da poterle controllare una ad una
        input=txtInput.split(" ")
        finalInput=[] #lista di richWord (con la parola in input e se è giuista o meno)
        finalInput.clear()
        if language=="italian":
            for word in input:
                finalInput.append(md.MultiDictionary().searchWord(word,"italian"))
        elif language=="english":
            for word in input:
                finalInput.append(md.MultiDictionary().searchWord(word, "english"))
        else:
            #se siamo qui è perforza spagnolo
            for word in input:
                finalInput.append(md.MultiDictionary().searchWord(word,"spanish"))
        """
        a questo punto abbiamo la lista finalInput con le parole e se sono state trovate o meno
        quindi possiamo stampare a video il risultato
        """
        for word in finalInput:
            if not word.corretta:
                print(word)


    def printMenu(self):
        print("______________________________\n" +
              "      SpellChecker 101\n"+
              "______________________________\n " +
              "Seleziona la lingua desiderata\n"
              "1. Italiano\n" +
              "2. Inglese\n" +
              "3. Spagnolo\n" +
              "4. Exit\n" +
              "______________________________\n")


def replaceChars(text):
    chars = "\\`*_{}[]()>#+-.!$%^;,=_~"
    for c in chars:
        # scambia il carattere in questione c con un ""
        text = text.replace(c, "")
    return text