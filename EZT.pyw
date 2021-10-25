"""Small ui app to ease transaltion between two languages

Usage:

    Meant to be used as a UI app only. For command line fuctionality refer directly to the googletrans module.
"""

# -*- coding: utf-8 -*-

# IMPORTS TODO ADD LIC INFO
import tkinter                      # UI
from tkinter.ttk import Combobox    # COMBOBOX
from googletrans import Translator  # TRANSLATION
#NOTE: the translation module uses google translate, but is not officially endorsed by google
#this fuctionaly may break when google decides to update it's APIs 
#lib installation command: pip install googletrans==3.1.0a0

# SETUP
translator = Translator()
mainWindow = tkinter.Tk()
topText    = ""
bottomText = ""
translateableLanguages = { 
    "Pol" : "pl",
    "Eng" : "en",
    "Slvk": "sk",
    "Blr" : "be"}

# FUNCTION DEFINITIONS
def translate(direction):
    """Translate text between TextBoxes
    
        Args:
            direction: string value(DOWN/UP), defines from which
            to which TextBox should the transaltion occur
        """
    if direction == "DOWN":
        fromLanguage = translateableLanguages[comboBoxTop.get()]
        toLanguage = translateableLanguages[comboBoxBottom.get()]
        fromTextBox = textBoxTop
        toTextBox = textBoxBottom
    else:
        fromLanguage = translateableLanguages[comboBoxBottom.get()]
        toLanguage = translateableLanguages[comboBoxTop.get()]
        fromTextBox = textBoxBottom
        toTextBox = textBoxTop
       
    toTextBox.delete("1.0","end")
    toTranslate = fromTextBox.get("1.0","end")
    translationResult = translator.translate(toTranslate, src=fromLanguage, dest=toLanguage)
    translated = translationResult.text
    toTextBox.insert("1.0", translated)

# UI WIDGETS (CONTROLS)
textBoxTop =            tkinter.Text(mainWindow, height=10)
buttonTransalateDown =  tkinter.Button(mainWindow, text= "Translate Down", command=lambda: translate("DOWN"))
buttonTransalateUp =    tkinter.Button(mainWindow, text= "Translate Up", command=lambda: translate("UP"))
textBoxBottom =         tkinter.Text(mainWindow, height=10)
labelTopDesc =          tkinter.Label(mainWindow, text = "Language " + "Top")
labelBottomDesc =       tkinter.Label(mainWindow, text = "Language " + "Bottom")
comboBoxTop =           Combobox(mainWindow, values = (list(translateableLanguages.keys())), width = 6)
comboBoxBottom =        Combobox(mainWindow, values = (list(translateableLanguages.keys())), width = 6)

# COMBO BOX DEFAULT VALUES 
comboBoxTop.set("Pol")
comboBoxBottom.set("Eng")


# UI LAYOUT
mainWindow.title("EZ Translate")
mainWindow.resizable(0, 0)
textBoxTop.grid(row = 0, columnspan=6, padx=5)
buttonTransalateDown.grid(row = 1, column = 2)
buttonTransalateUp.grid(row = 1, column = 3)
textBoxBottom.grid(row = 2, columnspan=6, padx=5)
comboBoxTop.grid(row = 1, column=0, padx=5)
comboBoxBottom.grid(row = 1, column = 5, padx=5)
labelTopDesc.grid(row =1, column = 1, padx=15)
labelBottomDesc.grid(row = 1, column = 4, padx=15)

# MAIN UI LOOP
mainWindow.mainloop()
