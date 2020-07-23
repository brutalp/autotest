from pywinauto.application import Application
import pywinauto

# TToolBar.TToolButton

keda = '"C:\\Program Files (x86)\\Bourevestnik\\KEDA\\kedaw.exe" -sim -spec=sim   -hvpsvst=0.2 --devdetflt=bra-135  --measerrordlg'
app = Application().start(keda)
keda_window = app.window(title='Предупреждение')
# Здесь кнопка Ок на русском
keda_window.Ок.click()
keda_window = app.window(title='Вход')
keda_window.Edit1.set_text('0')
# Здесь кнопка Ок на английском
keda_window.Ok.click()
# keda_window = app.window(title='Ошибка')
# # Здесь кнопка Ок на русском
# keda_window.Ок.click()
keda_window = app.window(title='Предупреждение')
# Здесь кнопка Ок на русском
keda_window.Ок.click()
keda_window = app.window(title='Предупреждение')
# Здесь кнопка Ок на русском
keda_window.Ок.click()
# app.window(title='КЭДА')['Static3'].print_control_identifiers()
# keda_window = app.window(title='КЭДА')['Static3']
keda_window = app.window(title='КЭДА')['TToolBar']
# наладка
# app.window(title='КЭДА')['TToolBar'].print_control_identifiers()
pywinauto.mouse.click(button='left', coords=(753, 338))
# app.window(title='КЭДА')['TToolBar'].Настройки.click()
# app.window(title='КЭДА').Наладка.click()
# keda_window.print_control_identifiers()
