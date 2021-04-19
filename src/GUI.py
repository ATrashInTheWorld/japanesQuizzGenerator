import tkinter as tk
import tkinter.filedialog
import Elements as elems
import json


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

        generateQuizz_button = tk.Button(self, text ="Generate new Quizz", command = generateNewQuizz)
        generateQuizz_button.pack(padx= 5, pady = 5)
        
        newKanjiBank_button = tk.Button(self, text="Create new Kanji bank", command=createNewKanjiBank)
        newKanjiBank_button.pack(padx=5, pady=5)
        
        newWordBank_button = tk.Button(self, text="Create new Word Bank", command=createNewWordBank)
        newWordBank_button.pack(padx=5, pady=5)

        newElemsBank_button = tk.Button(self, text="Create new Bank of Elements", command=createNewElemBank)
        newElemsBank_button.pack(padx=5, pady=5)

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


def saveBank(elemType):
    elements = []
    
    if elemType == "kanjis":
        for kanji in kanjiBank:
            elements.append({kanji.kanji:{"Meanings":kanji.getMeanings(), "Kunyomi":kanji.getKunr(), "Onyomi":kanji.getOnr()}})

    elif elemType == "words":
        for word in wordBank:
            elements.append({word.word:{"Reading":word.reading, "Definition":word.definition}})

    json_save = {elemType:elements}

    fileName = tk.filedialog.asksaveasfilename()
    if fileName:
        with open(fileName, 'w', encoding='utf8') as jsonFile:
            json.dump(json_save, jsonFile, indent=2, separators=(',',': '), ensure_ascii=False)



################################ QUIZZ related ############################
def generateNewQuizz():
    # x = Application.first_entry.get()
    print("Generating new quizz")

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


def createNewElemBank():
    print("New elems bank")

def modifyBank():
    print("modify bank")



### Boot
app = Application()
app.mainloop()