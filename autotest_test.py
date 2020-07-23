import pywinauto
from pywinauto.application import Application

app = Application().start("notepad.exe")
app.UntitledNotepad.menu_select("Справка->О программе")
app.Блокнотсведения.ОК.click()
pywinauto.mouse.click(button='right', coords=(753, 338))
