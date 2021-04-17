from appJar import gui
import UI_Methods as uim

def click(button):
    if button == "Generate New Quizz":
        uim.generateNewQuizz()
    elif button == "Create new Kanji bank":
        uim.createKanjiBank()
    elif button == "Create new Words bank":
        uim.createWordsBank()
    elif button == "Create a new Bank of Elements":
        uim.createElementsBank()
    elif button == "Modify an existing bank":
        uim.modifyExistingBank()


app = gui("Japanese Quizz Generator", "500x350")
app.addLabel("title", "Japanese Quizz Generator")
app.addButton("Generate New Quizz", click)
app.addButton("Create new Kanji bank", click)
app.addButton("Create new Words bank", click)
app.addButton("Create a new Bank of Elements", click)
app.addButton("Modify an existing bank", click)
app.go()



