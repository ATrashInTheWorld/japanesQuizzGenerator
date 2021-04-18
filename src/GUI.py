import tkinter as tk
import Elements as elems


### GLOBAL VARS
global app
global kanjiBank
kanjiBank = []


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


### Main window methods
def generateNewQuizz():
    # x = Application.first_entry.get()
    print("Generating new quizz")

################################ KANJI bank related ############################
class KanjiBank(tk.Toplevel):
    def __init__(self):
        tk.Toplevel.__init__(self)
        self.geometry('400x150')
        self.title("Create new Kanji bank")
        self.geometry("500x350")

        saveKanjiBank_button = tk.Button(self, text="Save Kanji Bank", command=saveKanjiBank)
        saveKanjiBank_button.pack()
        
        addKanjiToBank_button = tk.Button(self,text="+", command=addKanjiToListWindow)
        addKanjiToBank_button.pack()
        
        kanjiBankScroll = tk.Scrollbar(self)
        kanjiBankScroll.pack(side=tk.RIGHT, fill=tk.Y)
        
        KanjiBank.kanjiBankList = tk.Listbox(self, yscrollcommand = kanjiBankScroll.set)
        for kanji in kanjiBank:
            KanjiBank.kanjiBankList.insert(tk.END, kanji.toString())
            ### ADD DELETE button next to the kanji

        KanjiBank.kanjiBankList.pack(fill=tk.BOTH)
        kanjiBankScroll.config(command=KanjiBank.kanjiBankList.yview)

    def refreshKanjiBankHolder():
        KanjiBank.kanjiBankList.delete(0, tk.END)
        for kanji in kanjiBank:
            KanjiBank.kanjiBankList.insert(tk.END, kanji.toString())

# Kanji Window methodes
class KanjiForm(tk.Toplevel):
    def __init__(self):
        tk.Toplevel.__init__(self)
        self.geometry('400x150')
        self.title("Add kanji to bank")

        kanjiLabel = tk.Label(self, text="Kanji: ") 
        kanjiLabel.grid(row=0,column=0)
        KanjiForm.kanji_entry = tk.Entry(self, bd=2)
        KanjiForm.kanji_entry.grid(row=0,column=1)

        kunrLabel = tk.Label(self, text="Kunyomi \n(if multiple, separate with a ';'): ") 
        kunrLabel.grid(row=1,column=0)
        KanjiForm.kunr_entry = tk.Entry(self, bd=2)
        KanjiForm.kunr_entry.grid(row=1,column=1)

        onrLabel = tk.Label(self, text="Onyomi \n(if multiple, separate with a ';'): ")
        onrLabel.grid(row=2,column=0)
        KanjiForm.onr_entry = tk.Entry(self, bd=2)
        KanjiForm.onr_entry.grid(row=2,column=1)

        addToList_button = tk.Button(self, text="Add to list", 
                            command=addKanjiToList)
        addToList_button.grid(row=3,column=1)

def createNewKanjiBank():
     kanjiFormWindow = KanjiBank()

def addKanjiToListWindow():
    kanjiFormWindow = KanjiForm()

def addKanjiToList():
    k = KanjiForm.kanji_entry.get()
    kunr = KanjiForm.kunr_entry.get()
    onr = KanjiForm.onr_entry.get()
    kanji = elems.Kanji(k, kunr, onr)
    kanjiBank.append(kanji)
    KanjiForm.kanji_entry.delete(0, 'end')
    KanjiForm.kunr_entry.delete(0, 'end')
    KanjiForm.onr_entry.delete(0, 'end')
    KanjiBank.refreshKanjiBankHolder()

def saveKanjiBank():
    print("will save kanji bank")
    ## SAVE to a file as json format and add "type":"kanji" to identify file type
    ## Don't forget to erase the  kanji bank list


def createNewWordBank():
    print("New word Bank")

def createNewElemBank():
    print("New elems bank")

def modifyBank():
    print("modify bank")



### Boot
app = Application()
app.mainloop()