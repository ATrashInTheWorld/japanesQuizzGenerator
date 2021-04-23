import tkinter as tk
import tkinter.filedialog
import Elements as elems
import json
import webbrowser as web
# from os import getcwd
from os import path
from bs4 import BeautifulSoup as bs4
import random


### GLOBAL VARS
global app
global kanjiBank
global wordBank
kanjiBank = []
wordBank = []

## APP initialisation
class Application(tk.Tk):
     def __init__(self):
        tk.Tk.__init__(self)
        self.geometry('400x250')
        self.title('Japanese Quizz Generator')
        
        welcome_label = tk.Label(self, text = "Japanese Quizz Generator", font=10)
        welcome_label.pack(padx = 3, pady = 3)

        generateKanjiQuizz_button = tk.Button(self, text ="Generate new Kanji Quizz", command = lambda: generateNewQuizz("kanjis"))
        generateKanjiQuizz_button.pack(padx= 5, pady = 5)

        generateWordQuizz_button = tk.Button(self, text ="Generate new Word Quizz", command = lambda: generateNewQuizz("words"))
        generateWordQuizz_button.pack(padx= 5, pady = 5)
        
        newKanjiBank_button = tk.Button(self, text="Create new Kanji bank", command=createNewKanjiBank)
        newKanjiBank_button.pack(padx=5, pady=5)
        
        newWordBank_button = tk.Button(self, text="Create new Word Bank", command=createNewWordBank)
        newWordBank_button.pack(padx=5, pady=5)

        modifyBank_button = tk.Button(self, text="Modify an existing bank", command=modifyBank)
        modifyBank_button.pack(padx=5, pady=5)


class KanjiBank(tk.Toplevel):
    def __init__(self):
        tk.Toplevel.__init__(self)
        self.title("Create new Kanji bank")
        self.geometry("650x350")

        saveKanjiBank_button = tk.Button(self, text="Save Kanji Bank", command= lambda: saveBank("kanjis"))
        saveKanjiBank_button.pack()
        
        addKanjiToBank_button = tk.Button(self,text="+", command=addKanjiToListWindow)
        addKanjiToBank_button.pack()

        clearAll_button = tk.Button(self, text="Clear all", command=KanjiBank.clearAll)
        clearAll_button.pack()

        deleteSelected_button = tk.Button(self, text="Delete Selected", command=KanjiBank.deleteSelected)
        deleteSelected_button.pack()
        
        kanjiBankScroll = tk.Scrollbar(self)
        kanjiBankScroll.pack(side=tk.RIGHT, fill=tk.Y)
        
        KanjiBank.kanjiBankList = tk.Listbox(self, yscrollcommand = kanjiBankScroll.set)
        i=1
        for kanji in kanjiBank:
            KanjiBank.kanjiBankList.insert(tk.END, str(i)+". "+kanji.toString())
            i+=1

        KanjiBank.kanjiBankList.pack(fill=tk.BOTH)
        kanjiBankScroll.config(command=KanjiBank.kanjiBankList.yview)


    def refreshKanjiBankHolder():
        KanjiBank.kanjiBankList.delete(0, tk.END)
        i = 1
        for kanji in kanjiBank:
            KanjiBank.kanjiBankList.insert(tk.END, str(i)+". "+kanji.toString())
            i+=1

    def clearAll():
        kanjiBank.clear()
        KanjiBank.refreshKanjiBankHolder()

    def deleteSelected():
        if len(KanjiBank.kanjiBankList.curselection()) != 0:
            del kanjiBank[KanjiBank.kanjiBankList.curselection()[0]]
            KanjiBank.refreshKanjiBankHolder()


# Kanji Window methodes
class KanjiForm(tk.Toplevel):
    def __init__(self):
        tk.Toplevel.__init__(self)
        self.geometry('400x175')
        self.title("Add kanji to bank")

        kanjiLabel = tk.Label(self, text="Kanji: ") 
        kanjiLabel.grid(row=0,column=0)
        KanjiForm.kanji_entry = tk.Entry(self, bd=2)
        KanjiForm.kanji_entry.grid(row=0,column=1)

        meanLabel = tk.Label(self, text="Meaning(s)\n(if multiple, separate with a ';'): ") 
        meanLabel.grid(row=1,column=0)
        KanjiForm.meanings_entry = tk.Entry(self, bd=2)
        KanjiForm.meanings_entry.grid(row=1,column=1)

        kunrLabel = tk.Label(self, text="Kunyomi \n(if multiple, separate with a ';'): ") 
        kunrLabel.grid(row=2,column=0)
        KanjiForm.kunr_entry = tk.Entry(self, bd=2)
        KanjiForm.kunr_entry.grid(row=2,column=1)

        onrLabel = tk.Label(self, text="Onyomi \n(if multiple, separate with a ';'): ")
        onrLabel.grid(row=3,column=0)
        KanjiForm.onr_entry = tk.Entry(self, bd=2)
        KanjiForm.onr_entry.grid(row=3,column=1)

        addToList_button = tk.Button(self, text="Add to list", 
                            command=addKanjiToList)
        addToList_button.grid(row=4,column=1)


class WordBank(tk.Toplevel):
    def __init__(self):
        tk.Toplevel.__init__(self)
        self.title("Create new word bank")
        self.geometry("650x350")

        saveWordBank_button = tk.Button(self, text="Save word Bank", command= lambda: saveBank("words"))
        saveWordBank_button.pack()
        
        addWordToBank_button = tk.Button(self,text="+", command=addWordToListWindow)
        addWordToBank_button.pack()

        clearAll_button = tk.Button(self, text="Clear all", command=WordBank.clearAll)
        clearAll_button.pack()

        deleteSelected_button = tk.Button(self, text="Delete Selected", command=WordBank.deleteSelected)
        deleteSelected_button.pack()
        
        wordBankScroll = tk.Scrollbar(self)
        wordBankScroll.pack(side=tk.RIGHT, fill=tk.Y)
        
        WordBank.wordBankList = tk.Listbox(self, yscrollcommand = wordBankScroll.set)
        i = 1
        for word in wordBank:
            WordBank.wordBankList.insert(tk.END, str(i)+". "+word.toString())
            i+=1

        WordBank.wordBankList.pack(fill=tk.BOTH)
        wordBankScroll.config(command=WordBank.wordBankList.yview)

    def refreshWordBankHolder():
        WordBank.wordBankList.delete(0, tk.END)
        i = 1
        for word in wordBank:
            WordBank.wordBankList.insert(tk.END, str(i)+". "+word.toString())
            i +=1

    def clearAll():
        wordBank.clear()
        WordBank.refreshWordBankHolder()

    def deleteSelected():
        if len(WordBank.wordBankList.curselection()) != 0:
            del wordBank[WordBank.wordBankList.curselection()[0]]
            WordBank.refreshWordBankHolder()

# Words Form
class WordForm(tk.Toplevel):
    def __init__(self):
        tk.Toplevel.__init__(self)
        self.geometry('285x120')
        self.title("Add Word to bank")

        wordLabel = tk.Label(self, text="Word: ") 
        wordLabel.grid(row=0,column=0)
        WordForm.word_entry = tk.Entry(self, bd=2)
        WordForm.word_entry.grid(row=0,column=1)

        readingLabel = tk.Label(self, text="Reading: ") 
        readingLabel.grid(row=1,column=0)
        WordForm.reading_entry = tk.Entry(self, bd=2)
        WordForm.reading_entry.grid(row=1,column=1)

        defLabel = tk.Label(self, text="Definition: ")
        defLabel.grid(row=2,column=0)
        WordForm.def_entry = tk.Entry(self, bd=2)
        WordForm.def_entry.grid(row=2,column=1)

        addToList_button = tk.Button(self, text="Add to list", 
                            command=addWordToList)
        addToList_button.grid(row=3,column=1)


class QuizzFileSelection(tk.Toplevel):
    def __init__(self, quizzType):
        tk.Toplevel.__init__(self)
        self.geometry('600x350')
        self.title("Quizz Files Selection")

        #TODO Remove and empty this list
        #QuizzFileSelection.files_list = ["/home/dragonbug/Documents/Trashes/beta.json","/home/dragonbug/Documents/Trashes/beta.json","/home/dragonbug/Documents/Trashes/beta.json","/home/dragonbug/Documents/Trashes/beta.json","/home/dragonbug/Documents/Trashes/beta.json","/home/dragonbug/Documents/Trashes/beta.json","/home/dragonbug/Documents/Trashes/beta.json","/home/dragonbug/Documents/Trashes/beta.json","/home/dragonbug/Documents/Trashes/beta.json","/home/dragonbug/Documents/Trashes/beta.json","/home/dragonbug/Documents/Trashes/beta2.json"]
        QuizzFileSelection.files_list = []
        QuizzFileSelection.quizz_type = quizzType

        warning_label = tk.Label(self, text="Words and Kanji bank cannot be mixed.\nThe fille will be added, but the content will not be included.")
        warning_label.pack()

        QuizzFileSelection.add_file_button = tk.Button(self, text="Add a file", command=QuizzFileSelection.addFile)
        QuizzFileSelection.add_file_button.pack()

        QuizzFileSelection.remove_file_button = tk.Button(self, text="Remove Selected File", command=QuizzFileSelection.removeSelectedFile)
        QuizzFileSelection.remove_file_button.pack()

        QuizzFileSelection.clearall_file_button = tk.Button(self, text="Clear All Files", command=QuizzFileSelection.clearAllFiles)
        QuizzFileSelection.clearall_file_button.pack()

        QuizzFileSelection.setup_quizz_button = tk.Button(self, text="Setup Quizz", command=QuizzFileSelection.setupQuizz)
        QuizzFileSelection.setup_quizz_button.pack()

        QuizzFileSelection.fileScroll = tk.Scrollbar(self)
        QuizzFileSelection.fileScroll.pack(side=tk.RIGHT, fill=tk.Y)
        
        QuizzFileSelection.fileList = tk.Listbox(self, yscrollcommand = self.fileScroll.set)

        QuizzFileSelection.fileList.pack(fill=tk.BOTH)
        QuizzFileSelection.fileScroll.config(command=self.fileList.yview)

    def refreshFilesList():
        QuizzFileSelection.fileList.delete(0, tk.END)
        i = 1
        for fileName in QuizzFileSelection.files_list:
            QuizzFileSelection.fileList.insert(tk.END, str(i)+". "+fileName)
            i +=1

    def addFile():
        fileName = tk.filedialog.askopenfilename()
        if fileName:
            QuizzFileSelection.files_list.append(fileName)
            QuizzFileSelection.refreshFilesList()
    
    def removeSelectedFile():
        if len(QuizzFileSelection.fileList.curselection()) != 0:
            del QuizzFileSelection.files_list[QuizzFileSelection.fileList.curselection()[0]]
            QuizzFileSelection.refreshFilesList()

    def clearAllFiles():
        QuizzFileSelection.files_list.clear()
        QuizzFileSelection.refreshFilesList()

    def setupQuizz():
        elements_list = []
        for fileName in QuizzFileSelection.files_list:
                elements = open(fileName, encoding='utf8')
                data = json.load(elements)
                if list(data.keys())[0] == "kanjis" and QuizzFileSelection.quizz_type=="kanjis":
                    for element in data[QuizzFileSelection.quizz_type]:
                        kanji = list(element.keys())[0]
                        meanings = ';'.join(element[kanji]["Meanings"])
                        kunyomi = ';'.join(element[kanji]["Kunyomi"])
                        onyomi = ';'.join(element[kanji]["Onyomi"])
                        elements_list.append(elems.Kanji(kanji, meanings, kunyomi, onyomi))

                elif list(data.keys())[0] == "words" and QuizzFileSelection.quizz_type=="words":
                    for element in data[QuizzFileSelection.quizz_type]:
                        word = list(element.keys())[0]
                        elements_list.append(elems.Word(word, element[word]["Reading"], element[word]["Definition"]))

        QuizzGenerator(QuizzFileSelection.quizz_type, elements_list)

## Quizz generation
class QuizzGenerator(tk.Toplevel):
    def __init__(self, quizzType, elements):
        tk.Toplevel.__init__(self)
        self.geometry('700x650')
        self.title("Quizz Generator")

        QuizzGenerator.quizz_type = quizzType
        QuizzGenerator.selected = elements
        QuizzGenerator.unselected = []

        QuizzGenerator.move_selected = tk.Button(self, text="Move selected", command=QuizzGenerator.moveSelected)
        QuizzGenerator.move_selected.pack()

        QuizzGenerator.select_all = tk.Button(self, text="Select All", command=QuizzGenerator.selectAll)
        QuizzGenerator.select_all.pack()

        QuizzGenerator.select_all = tk.Button(self, text="Unselect All", command=QuizzGenerator.unselectAll)
        QuizzGenerator.select_all.pack()

        QuizzGenerator.selectedLabel = tk.Label(self, text="Selected items to be quizzed on")
        QuizzGenerator.selectedLabel.pack()
        QuizzGenerator.selectedList = tk.Listbox(self, height=7)
        i = 1
        for element in QuizzGenerator.selected:
            QuizzGenerator.selectedList.insert(tk.END, str(i)+". "+element.toString())
            i+=1
        QuizzGenerator.selectedList.pack(fill=tk.X)

        QuizzGenerator.unselectedLabel = tk.Label(self, text="Unselected items to be quizzed on")
        QuizzGenerator.unselectedLabel.pack()
        QuizzGenerator.unselectedList = tk.Listbox(self, height=7)
        QuizzGenerator.unselectedList.pack(fill=tk.X)

        QuizzGenerator.question = tk.StringVar()
        QuizzGenerator.answers = tk.StringVar()

        QuizzGenerator.questionLabel = tk.Label(self, text="Question Element")
        QuizzGenerator.questionLabel.pack()
        if quizzType == "kanjis":
            QuizzGenerator.kanji_rb = tk.Radiobutton(self, text="Kanji", variable=QuizzGenerator.question, value="kanji")
            QuizzGenerator.meaning_rb = tk.Radiobutton(self, text="Meaning", variable=QuizzGenerator.question, value="meanings")
            QuizzGenerator.kunyomi_rb = tk.Radiobutton(self, text="Kunyomi", variable=QuizzGenerator.question, value="kunr")
            QuizzGenerator.onyomi_rb = tk.Radiobutton(self, text="Onyomi", variable=QuizzGenerator.question, value="onr")
            QuizzGenerator.kanji_rb.pack()
            QuizzGenerator.meaning_rb.pack()
            QuizzGenerator.kunyomi_rb.pack()
            QuizzGenerator.onyomi_rb.pack()
        elif quizzType == "words":
            QuizzGenerator.word_rb = tk.Radiobutton(self, text="Word", variable=QuizzGenerator.question, value="word")
            QuizzGenerator.reading_rb = tk.Radiobutton(self, text="Reading", variable=QuizzGenerator.question, value="reading")
            QuizzGenerator.def_rb = tk.Radiobutton(self, text="Definition", variable=QuizzGenerator.question, value="definition")
            QuizzGenerator.word_rb.pack()
            QuizzGenerator.reading_rb.pack()
            QuizzGenerator.def_rb.pack()
        
        QuizzGenerator.answeresLabel = tk.Label(self, text="Multiple Choices Answere Elements")
        QuizzGenerator.answeresLabel.pack()

        if quizzType == "kanjis":
            QuizzGenerator.kanji_rb = tk.Radiobutton(self, text="Kanji", variable=QuizzGenerator.answers, value="kanji")
            QuizzGenerator.meaning_rb = tk.Radiobutton(self, text="Meaning", variable=QuizzGenerator.answers, value="meanings")
            QuizzGenerator.kunyomi_rb = tk.Radiobutton(self, text="Kunyomi", variable=QuizzGenerator.answers, value="kunr")
            QuizzGenerator.onyomi_rb = tk.Radiobutton(self, text="Onyomi", variable=QuizzGenerator.answers, value="onr")
            QuizzGenerator.kanji_rb.pack()
            QuizzGenerator.meaning_rb.pack()
            QuizzGenerator.kunyomi_rb.pack()
            QuizzGenerator.onyomi_rb.pack()
        elif quizzType == "words":
            QuizzGenerator.word_rb = tk.Radiobutton(self, text="Word", variable=QuizzGenerator.answers, value="word")
            QuizzGenerator.reading_rb = tk.Radiobutton(self, text="Reading", variable=QuizzGenerator.answers, value="reading")
            QuizzGenerator.def_rb = tk.Radiobutton(self, text="Definition", variable=QuizzGenerator.answers, value="definition")
            QuizzGenerator.word_rb.pack()
            QuizzGenerator.reading_rb.pack()
            QuizzGenerator.def_rb.pack()
        
        QuizzGenerator.generateQuizz_button = tk.Button(self, text="Generate Quizz with current settings", command=QuizzGenerator.generateQuizz)
        QuizzGenerator.generateQuizz_button.pack()

    def refreshLists():
        QuizzGenerator.selectedList.delete(0, tk.END)
        i = 1
        for element in QuizzGenerator.selected:
            QuizzGenerator.selectedList.insert(tk.END, str(i)+". "+element.toString())
            i+=1

        QuizzGenerator.unselectedList.delete(0, tk.END)
        i = 1
        for element in QuizzGenerator.unselected:
            QuizzGenerator.unselectedList.insert(tk.END, str(i)+". "+element.toString())
            i+=1


    def moveSelected():
        if len(QuizzGenerator.selectedList.curselection()) != 0:
            element = QuizzGenerator.selected[QuizzGenerator.selectedList.curselection()[0]]
            del QuizzGenerator.selected[QuizzGenerator.selectedList.curselection()[0]]
            QuizzGenerator.unselected.append(element)
        elif len(QuizzGenerator.unselectedList.curselection()) != 0:
            element = QuizzGenerator.unselected[QuizzGenerator.unselectedList.curselection()[0]]
            del QuizzGenerator.unselected[QuizzGenerator.unselectedList.curselection()[0]]
            QuizzGenerator.selected.append(element)
        QuizzGenerator.refreshLists()

    def selectAll():
        QuizzGenerator.selected += QuizzGenerator.unselected
        QuizzGenerator.unselected.clear()
        QuizzGenerator.refreshLists()


    def unselectAll():
        QuizzGenerator.unselected += QuizzGenerator.selected
        QuizzGenerator.selected.clear()
        QuizzGenerator.refreshLists()


    def generateQuizz():
        quizzType = QuizzGenerator.quizz_type
        question = str(QuizzGenerator.question.get())
        answers = str(QuizzGenerator.answers.get())
        answersElement = []

        if question != None and answers != None:
            quizzPage = open(path.abspath("quizzPage.html"), 'r', encoding='utf-8', errors='ignore')
            soup = bs4(quizzPage.read(), 'html.parser')

            questionsHtml = QuizzGenerator.generateHtmlQuestions(QuizzGenerator.selected, question, answers)
            questionsDiv = soup.find(id="questions")
            questionsDiv.clear()
            questionsDiv.append(bs4(questionsHtml, 'html.parser'))

            with open(path.abspath("quizzPage.html"), 'w', encoding='utf-8', errors='ignore') as quizzFilePage:
                quizzFilePage.write(str(soup))

            web.open('file://'+path.abspath("quizzPage.html"))


    def generateHtmlQuestions(elements, question, answers):
        scrambledElements = QuizzGenerator.shuffleList(elements)

        htmlTxt = ""
        if len(elements) > 4:
            i = 1
            for element in scrambledElements:
                randomAns = [element]
                while len(randomAns) != 4:
                    extraAns = elements[random.randint(0,len(elements)-1)]
                    if extraAns not in randomAns and extraAns.getAttr(answers)!=element.getAttr(answers):
                        randomAns.append(extraAns)
                
                randomPositions = QuizzGenerator.shuffleList([0,1,2,3])

                print(element.getAttr(question))
                htmlTxt += "<p id='pq"+str(i)+"'>"+str(i)+". "+element.getAttr(question)+"<br>"
                for position in randomPositions:
                    qNumber = str(i)
                    answValue = randomAns[position].getAttr(answers)
                    htmlTxt += "<input type='radio' name='q"+qNumber+"' value='"+answValue+"' id='"+qNumber+"-"+answValue+"'>"
                    htmlTxt += "<label for='"+qNumber+"-"+answValue+"'>"+answValue+"</label> &nbsp &nbsp"

                htmlTxt += "</p>"
                i +=1

            answersElement = []
            for element in scrambledElements:
                answersElement.append(element.getAttr(answers))
            htmlTxt += "<input type='hidden' id='answersList' value='"+'---'.join(answersElement)+"'>"
            htmlTxt += "<input type='hidden' id='totalQuestions'  value='"+str(i-1)+"'>"
        
        else:
            htmlTxt += "<p>Need at least 5 elements in your selected list or bank </p>"

        print()

        return htmlTxt


    def shuffleList(elemList):
        shuffle = elemList[:]
        random.shuffle(shuffle)
        return shuffle




# Modify an existing bank of Kanjis or Words
class BankModifier(tk.Toplevel):
    def __init__(self):
        tk.Toplevel.__init__(self)
        self.geometry('350x75')
        self.title("Change an existing Bank")

        BankModifier.choseFile_button = tk.Button(self, text="Open a file to change (kanjis or words)", command=BankModifier.openFile)
        BankModifier.choseFile_button.pack(pady=25)

    def openFile():
        fileName = tk.filedialog.askopenfilename()
        if fileName:
            data = json.load(open(fileName, encoding='utf8'))
            fileType = list(data.keys())[0]

            if fileType == "kanjis":
                kanjiBank.clear()
                for element in data[fileType]:
                    kanji = list(element.keys())[0]
                    meanings = ';'.join(element[kanji]["Meanings"])
                    kunyomi = ';'.join(element[kanji]["Kunyomi"])
                    onyomi = ';'.join(element[kanji]["Onyomi"])
                    kanjiBank.append(elems.Kanji(kanji, meanings, kunyomi, onyomi))
                KanjiBank()

            elif fileType == "words":
                wordBank.clear()
                for element in data[fileType]:
                    word = list(element.keys())[0]
                    wordBank.append(elems.Word(word, element[word]["Reading"], element[word]["Definition"]))
                WordBank()



def saveBank(elemType):
    elements = []
    
    if elemType == "kanjis":
        for kanji in kanjiBank:
            elements.append({kanji.kanji:{"Meanings":kanji.getMeanings(), "Kunyomi":kanji.getKunr(), "Onyomi":kanji.getOnr()}})

    elif elemType == "words":
        for word in wordBank:
            elements.append({word.word:{"Reading":word.reading, "Definition":word.definition}})

    json_save = {elemType:elements}
    # print(json_save)

    fileName = tk.filedialog.asksaveasfilename()
    if fileName:
        with open(fileName, 'w', encoding='utf8') as jsonFile:
            json.dump(json_save, jsonFile, indent=2, separators=(',',': '), ensure_ascii=False)


def generateNewQuizz(quizzType):
    QuizzFileSelection(quizzType)

################################ KANJI bank related ############################
def createNewKanjiBank():
     kanjiFormWindow = KanjiBank()

def addKanjiToListWindow():
    kanjiFormWindow = KanjiForm()

def addKanjiToList():
    k = KanjiForm.kanji_entry.get()
    m = KanjiForm.meanings_entry.get()
    kunr = KanjiForm.kunr_entry.get()
    onr = KanjiForm.onr_entry.get()
    kanji = elems.Kanji(k, m, kunr, onr)
    kanjiBank.append(kanji)
    KanjiForm.kanji_entry.delete(0, 'end')
    KanjiForm.meanings_entry.delete(0, 'end')
    KanjiForm.kunr_entry.delete(0, 'end')
    KanjiForm.onr_entry.delete(0, 'end')
    KanjiBank.refreshKanjiBankHolder()
############################# END KANJI bank related ############################

################################ WORD bank related #############################
def createNewWordBank():
    wordBankWindow = WordBank()

def addWordToListWindow():
    workAddForm = WordForm()

def addWordToList():
    w = WordForm.word_entry.get()
    r = WordForm.reading_entry.get()
    d = WordForm.def_entry.get()
    word = elems.Word(w, r, d)
    wordBank.append(word)
    WordForm.word_entry.delete(0, 'end')
    WordForm.reading_entry.delete(0, 'end')
    WordForm.def_entry.delete(0, 'end')
    WordBank.refreshWordBankHolder()
############################ END WORD bank related #############################

def modifyBank():
    BankModifier()



### Boot
app = Application()
app.mainloop()