import time

import multiDictionary as md

class SpellChecker:

    def __init__(self):
        pass

    def handleSentence(self, txtIn, language):
        start_time = time.perf_counter()
        txtInput=replaceChars(txtIn.lower())
        #dapprima salviamoci le parole in un vettore in modo da poterle controllare una ad una
        input=txtInput.split(" ")
        input=eliminaSpazi(input)
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
        end_time=time.perf_counter()
        elapsed_time=end_time-start_time
        print("------------------------------------\n"+
              "    Le parole sbagliate sono   ")
        for word in finalInput:
            if not word.corretta:
                print(word)
        print(f"Tempo di ricerca con contains:{elapsed_time}")


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
def eliminaSpazi(input):
    #restituisce un vettore di str che non contenga spazi
    inputCorretto=[]
    for i in input:
        if i!="":
            inputCorretto.append(i)
    return inputCorretto

