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

    def setWord(self, word):
        self.word = word

    def setReading(self, Reading):
        self.reading = reading

    def setDefinition(self, definition):
        self.definition = definition


'''
Kanji: extends Element. holds kanji and its readings
'''
class Kanji(Element):
    def __init__(self, kanji, kunr, onr):
        self.kanji = kanji
        self.onr = onr
        self.kunr = kunr

    def getKanji(self):
        return self.kanji

    def getOnr(self):
        return self.onr.split(';')

    def getKunr(self):
        return self.kunr.split(';')

    def setKanji(self, kanji):
        self.kanji = kanji

    def setOnr(self, onr):
        self.onr = onr

    def setKunr(self, kunr):
        self.kunr = kunr
    
    def toString(self):
        kanjiVals = self.kanji+"   Kunyomi:"
        for kunr in self.kunr.split(';'):
            kanjiVals +=" -"+kunr
        kanjiVals += "   Onyomi"
        for onr in self.onr.split(';'):
            kanjiVals +=" -"+onr

        return kanjiVals