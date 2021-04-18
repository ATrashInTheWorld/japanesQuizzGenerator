from appJar import gui
import UI_Methods as uim
import Elements

######### GENERAL FUNCTIONS
def addToolBarButtons():
    app.addButton("Save to new file", uim.saveDiscarToolbar)

def closeSubWindow():
    app.hideAllSubWindows(useStopFunction=False)


######### KANJI UI Buttons
def addNewKanji():
    app.startSubWindow("New kanji",title="Create New Kanji", modal=True)
    app.setSize(500,300)
    # app.setStopFunction(stopSubWindow)
    app.showSubWindow("New kanji", "")



######### MAIN UI BUTTONS
def generateNewQuizz():
    print("new Quizz generation")

def createKanjiBank():
    print("create Kanji Bank")
    kanjiBank = []
    app.startSubWindow("kanji", modal=True)
    app.setStopFunction(closeSubWindow)
    app.setSize(600,400)
    app.showSubWindow("kanji", "")
    addToolBarButtons()
    app.addButton("+", addNewKanji)
    app.startScrollPane("Kanji Bank")
    for kanji in kanjiBank:
        app.addLabel(kanji.getKanji(), kanji.toString())

def createWordsBank():
    print("create Words Bank")

def createElementsBank():
    print("create elements Bank")

def modifyExistingBank():
    print("modifiyng word Bank")


def click(button):
    if button == "Generate New Quizz":
        generateNewQuizz()
    elif button == "Create new Kanji bank":
        createKanjiBank()
    elif button == "Create new Words bank":
        createWordsBank()
    elif button == "Create a new Bank of Elements":
        createElementsBank()
    elif button == "Modify an existing bank":
        modifyExistingBank()

global app
global kanjiBank

app = gui("Japanese Quizz Generator", "500x350")
app.addLabel("title", "Japanese Quizz Generator")
app.addButton("Generate New Quizz", click)
app.addButton("Create new Kanji bank", click)
app.addButton("Create new Words bank", click)
app.addButton("Create a new Bank of Elements", click)
app.addButton("Modify an existing bank", click)
app.go()



