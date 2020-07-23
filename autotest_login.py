from pywinauto.application import Application
PASSWORD = '0'

keda = '"C:\\Program Files (x86)\\Bourevestnik\\KEDA\\kedaw.exe" -sim -spec=sim   -hvpsvst=0.2 --devdetflt=bra-135  --measerrordlg'
app = Application().start(keda)
# Здесь кнопка Ок на русском
app.window(title='Предупреждение').Ок.click()
app.window(title='Вход').Edit1.set_text(PASSWORD)
# Здесь кнопка Ок на английском
app.window(title='Вход').Ok.click()
# Здесь кнопка Ок на русском
app.window(title='Предупреждение').Ок.click()
# Здесь кнопка Ок на русском
app.window(title='Предупреждение').Ок.click()
app.window(title='КЭДА').Выходизпрограммы.click()
app.window(title='Подтверждение').Да.click()

