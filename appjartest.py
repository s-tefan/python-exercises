# import the library
from appJar import gui


def uppdatera(btn):
    app.setLabel("text",app.getEntry("e1"))


# create a GUI variable called app
app = gui()
app.addLabel("title", "Welcome to appJar")
app.setLabelBg("title", "red")
app.addEntry("e1")
app.setEntryDefault("e1", "Skriv här")
app.addLabel("text","...")
app.addButton("Uppdatera",uppdatera)
app.setEntrySubmitFunction("e1",uppdatera)
app.go()