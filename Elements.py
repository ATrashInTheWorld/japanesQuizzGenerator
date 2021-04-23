'''
This Contains The possible elements that can be created:
Element <|--- Word
Element <|--- Kanji
'''

'''
General object for elements. Can be used to generate any kind of thing
'''
class Element:
    def __init__(self, values):
        self.values = values
    
    def getValue(self):
        return self.values

    def setValues(self,values):
        self.values = values


'''
Word: extends Element. Holds a words an its characteristics
'''
class Word(Element):
    def __init__(self, word, reading, definition):
        self.word = word
        self.reading = reading
        self.definition = definition

    def getWord(self):
        return self.word

    def getReading(self):
        return self.reading

    def getDefinition(self):
        return self.definition

    def getAttr(self,attr):
        if attr == "word":
            return self.word
        elif attr == "reading":
            return self.reading
        elif attr == "definition":
            return self.definition

    def toString(self):
        wordVals = self.word+"   Reading: "+self.reading+"   Definition: "+self.definition
        return wordVals


'''
Kanji: extends Element. holds kanji and its readings
'''
class Kanji(Element):
    def __init__(self, kanji, meanings, kunr, onr):
        self.kanji = kanji
        self.meanings = meanings
        self.onr = onr
        self.kunr = kunr

    def getKanji(self):
        return self.kanji

    def getMeanings(self):
        return self.meanings.split(';')

    def getOnr(self):
        return self.onr.split(';')

    def getKunr(self):
        return self.kunr.split(';')

    def getAttr(self, attr):
        if attr == "kanji":
            return self.kanji
        elif attr == "meanings":
            return self.meanings
        elif attr == "onr":
            return self.onr
        elif attr == "kunr":
            return self.kunr
    
    def toString(self):
        kanjiVals = self.kanji+"   Meaning: "
        for mean in self.meanings.split(';'):
            kanjiVals +=" -"+mean
        kanjiVals+="   Kunyomi:"
        for kunr in self.kunr.split(';'):
            kanjiVals +=" -"+kunr
        kanjiVals += "   Onyomi"
        for onr in self.onr.split(';'):
            kanjiVals +=" -"+onr

        return kanjiVals