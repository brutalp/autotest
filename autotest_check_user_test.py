from pywinauto.application import Application

keda = '"C:\\Program Files (x86)\\Bourevestnik\\KEDA\\kedaw.exe" -sim -spec=sim   -hvpsvst=0.2 --devdetflt=bra-135  --measerrordlg'
app = Application().start(keda)
keda_window = app.window(title='Предупреждение')
# Здесь кнопка Ок на русском
keda_window.Ок.click()
keda_window = app.window(title='Вход')
keda_window.Edit1.set_text('test')
keda_window.Edit2.set_text('test')
keda_window.Edit3.set_text('test')
# Здесь кнопка Ок на английском
keda_window.Ok.click()
# Здесь кнопка Ок на русском
app.window(title='Информация').Ок.click()
app.window(title='КЭДА').Выходизпрограммы.click()
app.window(title='Подтверждение').Да.click()
