from pywinauto.application import Application
import pywinauto
import time
import datetime
import pyperclip
import random
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
keda_window.Edit4.set_text('Тестовая программа-' + str(random.randrange(0, 50, 1)) + ' ' + str(datetime.datetime.date(DATE)))
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
time.sleep(1)
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
keda_window = app.window(title_re='Состав градуировочных образцов')
keda_window.Добавить.click()
# pywinauto.mouse.click(button='left', coords=(421, 351))
keda_window = app.window(title='Добавить образцы')
keda_window.Edit0.set_text('5')
keda_window.Ок.click()
pyperclip.copy("""ГО-1	0	5	0
ГО-2	5	0	20
ГО-3	50	30	0
ГО-4	70	100	100
ГО-5	100	70	50
""")
pywinauto.mouse.click(button='left', coords=(438, 558))
time.sleep(1)
pywinauto.keyboard.send_keys("^v")
# pywinauto.keyboard.send_keys('^v')
time.sleep(15)

# Сохранить
keda_window = app.window(title_re='Состав градуировочных образцов')
keda_window.Сохранить.click()

# градуировка аналитической программы
pywinauto.mouse.click(button='left', coords=(249, 644))
# измерение градуировочных образцов
pywinauto.mouse.click(button='left', coords=(53, 703))
keda_window = app.window(title='Измерение градуировочных образцов')
keda_window.Edit0.click()
pywinauto.keyboard.send_keys('С')
time.sleep(1)
keda_window.ToolbarСтарт.click()
time.sleep(5)
# pywinauto.mouse.click(button='left', coords=(196, 80))
pyperclip.copy("""100	100	100	100	100
10	10	10	10	10
20	30	40	50	60
20	20	20	20	20
0	0	0	0	0
60	50	40	30	20
""")
pywinauto.keyboard.send_keys('^v')
# time.sleep(5)
# pywinauto.keyboard.send_keys("{VK_LSHIFT down}"
#                              "{VK_LCONTROL down}"
#                              "{F8 down}"
#                              "{VK_LSHIFT up}"
#                              "{VK_LCONTROL up}"
#                              "{F8 up}"
#                              )
time.sleep(5)
keda_window = app.window(title_re='Ввод интенсивностей')
keda_window.Применить.click()
time.sleep(5)
keda_window = app.window(title_re='Измерение градуировочных образцов')
keda_window.Сохранить.click()
