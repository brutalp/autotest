from pywinauto.application import Application
import pywinauto
import time


keda = '"C:\\Program Files (x86)\\Bourevestnik\\KEDA\\kedaw.exe" -sim -spec=sim   -hvpsvst=0.2 --devdetflt=bra-135  --measerrordlg'
app = Application().start(keda)
keda_window = app.window(title='Предупреждение')
# Здесь кнопка Ок на русском
keda_window.Ок.click()
keda_window = app.window(title='Вход')
keda_window.Edit2.set_text('0')
# Здесь кнопка Ок на английском
keda_window.Ok.click()

time.sleep(2)
# настройка программы
pywinauto.mouse.click(button='left', coords=(743, 611))
# вкладка учётные записи
pywinauto.mouse.click(button='left', coords=(523, 141))
# добавить
pywinauto.mouse.click(button='left', coords=(351, 214))
# app.window(title='Добавление нового пользователя').print_control_identifiers()
app.window(title='Добавление нового пользователя').Edit2.set_text('test')
app.window(title='Добавление нового пользователя').Edit3.set_text('test')
app.window(title='Добавление нового пользователя').Добавить.click()
app.window(title='Настройки').Сохранить.click()

# выход из программы
app.window(title='КЭДА').Выходизпрограммы.click()
app.window(title='Подтверждение').Да.click()
