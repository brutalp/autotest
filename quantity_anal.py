from pywinauto.application import Application
import pywinauto
import time
import datetime
DATE = datetime.datetime.now()

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
# количественный анализ
pywinauto.mouse.click(button='left', coords=(734, 473))
time.sleep(1)
# создать
pywinauto.mouse.click(button='left', coords=(82, 90))
keda_window = app.window(title='Создание аналитической программы')
# кратность измерения edit1
keda_window.Edit4.set_text('Тестовая программа ' + str(datetime.datetime.date(DATE)))
# шифр
pywinauto.mouse.click(button='left', coords=(876, 417))
pywinauto.keyboard.send_keys('ХЗ')
keda_window.Создать.click()
# линии, условия измерения
pywinauto.mouse.click(button='left', coords=(249, 307))
keda_window = app.window(title='Редактирование')
keda_window.Добавить.click()
keda_window.Добавить.click()
# Uкв режим 2
pywinauto.mouse.click(button='left', coords=(912, 433))
pywinauto.keyboard.send_keys('25')
# клик в сторону, чтобы убрать всплывающее окно
pywinauto.mouse.click(button='left', coords=(912, 500))
# Uкв режим 3
pywinauto.mouse.click(button='left', coords=(920, 670))
pywinauto.keyboard.send_keys('30')
# клик в сторону, чтобы убрать всплывающее окно
pywinauto.mouse.click(button='left', coords=(920, 700))

# измеряемые линии 1
pywinauto.mouse.click(button='left', coords=(875, 264))
# добавить
pywinauto.mouse.click(button='left', coords=(292, 539))
# AL
pywinauto.mouse.click(button='left', coords=(1210, 366))
# Si
pywinauto.mouse.click(button='left', coords=(1280, 365))
keda_window = app.window(title='Периодическая таблица химических элементов')
keda_window.Сохранить.click()
# закрываем
pywinauto.mouse.click(button='left', coords=(875, 264))

# измеряемые линии 2
pywinauto.mouse.click(button='left', coords=(873, 503))
# добавить
pywinauto.mouse.click(button='left', coords=(295, 779))
# Ti
pywinauto.mouse.click(button='left', coords=(567, 436))
keda_window = app.window(title='Периодическая таблица химических элементов')
keda_window.Сохранить.click()
# закрываем
pywinauto.mouse.click(button='left', coords=(873, 503))

# измеряемые линии 3
pywinauto.mouse.click(button='left', coords=(875, 741))
# добавить
pywinauto.mouse.click(button='left', coords=(292, 1016))
# Fe
pywinauto.mouse.click(button='left', coords=(848, 437))
# Ni
pywinauto.mouse.click(button='left', coords=(993, 436))
keda_window = app.window(title='Периодическая таблица химических элементов')
keda_window.Сохранить.click()
# закрываем
pywinauto.mouse.click(button='left', coords=(875, 741))
keda_window = app.window(title='Редактирование')
keda_window.Сохранить.click()

# определяемые элементы
pywinauto.mouse.click(button='left', coords=(161, 397))
# Ti
pywinauto.mouse.click(button='left', coords=(565, 438))
# Fe
pywinauto.mouse.click(button='left', coords=(848, 437))
# Al
pywinauto.mouse.click(button='left', coords=(1210, 366))
keda_window = app.window(title='Периодическая таблица химических элементов')
keda_window.Сохранить.click()

# градуировочные образцы
pywinauto.mouse.click(button='left', coords=(210, 456))
# добавить
pywinauto.mouse.click(button='left', coords=(421, 351))
keda_window = app.window(title='Добавить образцы')
keda_window.Edit0.set_text('5')
keda_window.Ок.click()
# ГО 1
pywinauto.mouse.click(button='left', coords=(438, 558))
pywinauto.keyboard.send_keys('ГО-1')
# ГО 2
pywinauto.mouse.click(button='left', coords=(434, 602))
pywinauto.keyboard.send_keys('ГО-2')
# ГО 3
pywinauto.mouse.click(button='left', coords=(439, 640))
pywinauto.keyboard.send_keys('ГО-3')
# ГО 4
pywinauto.mouse.click(button='left', coords=(454, 681))
pywinauto.keyboard.send_keys('ГО-4')
# ГО 5
pywinauto.mouse.click(button='left', coords=(447, 713))
pywinauto.keyboard.send_keys('ГО-5')
# Сохранить
keda_window = app.window(title_re='Состав градуировочных образцов')
keda_window.Сохранить.click()
# pywinauto.mouse.click(button='left', coords=(1164, 790))
# keda_window.print_control_identifiers()

# градуировка аналитической программы
pywinauto.mouse.click(button='left', coords=(249, 644))
# измерение градуировочных образцов
pywinauto.mouse.click(button='left', coords=(53, 703))
keda_window = app.window(title='Измерение градуировочных образцов')
keda_window.Edit0.click()
pywinauto.keyboard.send_keys('С')
time.sleep(1)
keda_window.ToolbarСтарт.click()
pywinauto.keyboard.send_keys("{VK_LSHIFT down}"
                             "{VK_LCONTROL down}"
                             "{F8 down}")
keda_window = app.window(title_re='Ввод интенсивностей')
keda_window.Применить.click()
