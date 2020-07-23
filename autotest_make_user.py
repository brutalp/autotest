from pywinauto.application import Application
import time

keda = '"C:\\Program Files (x86)\\Bourevestnik\\KEDA\\kedaw.exe"'
app = Application().start(keda)
# app = Application(backend='uia').start(keda)
# window = app.window()
window = app.window(title='Предупреждение')
# Здесь кнопка Ок на русском
window.Ок.click()
window = app.window(title='Вход')
window.Edit1.set_text('BRAlkzDOBRA1')
window.Edit2.set_text('BRAlkzDOBRA1')
# time.sleep(5)
# Здесь кнопка Ок на английском
window.Ok.click()
# window = app.window()
window = app.window(title='Подтверждение')
window.Да.click()
window = app.window(title='Ошибка')
# window = app.window()
# Здесь кнопка Ок на русском
window.Ок.click()
window = app.window(title='КЭДА')
window.Настройка.click()
