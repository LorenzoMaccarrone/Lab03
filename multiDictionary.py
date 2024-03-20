import dictionary as d
import richWord as rw


class MultiDictionary:


    def __init__(self):
        pass

    def printDic(self, language):
        pass

    def searchWord(self, words, language):
        #restituisce una richWord con lattributo corretta a true se è stata trovata tale parola
        #o false se non è stata trovata
        dict=d.Dictionary()
        if language=="italian":
            dict.loadDictionary("./resources/Italian.txt")
            dizionarioItaliano=dict.dict #(dict.dict=getter method for _self.dict of the dictionary class)
            richWord = rw.RichWord(words)
            for word in dizionarioItaliano:
                word=word.rstrip('\n')
                if words==word:
                    richWord.corretta=True
                    return richWord
                else:
                    richWord.corretta=False
            return richWord

        elif language=="english":
            dict.loadDictionary("./resources/English.txt")
            dizionarioInglese= dict.dict  # (dict.dict=getter method for _self.dict of the dictionary class)
            richWord = rw.RichWord(words)
            for word in dizionarioInglese:
                word = word.rstrip('\n')
                if words == word:
                    richWord.corretta=True
                    return richWord
                else:
                    richWord.corretta=False
            return richWord
        else:
            #se siamo qui è perforza spagnolo
            dict.loadDictionary("./resources/Spanish.txt")
            dizionarioSpagnolo = dict.dict  # (dict.dict=getter method for _self.dict of the dictionary class)
            richWord = rw.RichWord(words)
            for word in dizionarioSpagnolo:
                word = word.rstrip('\n')
                if words == word:
                    richWord.corretta=True
                    return richWord
                else:
                    richWord.corretta=False
            return richWord






