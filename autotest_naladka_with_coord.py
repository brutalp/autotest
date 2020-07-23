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
# наладка
pywinauto.mouse.click(button='left', coords=(753, 338))
keda_window = app.window(title='Наладка-W БРА-135F')

keda_window.Приборнаяградуировка.click()
# жмём на кнопку отменить, нужно будет исправить, когда исправят баг с нонейм окном
pywinauto.mouse.click(button='left', coords=(1804, 1007))

# Настройка и диагностика
pywinauto.mouse.click(button='left', coords=(222, 477))
# keda_window.Настройкаидиагностика.click()
keda_window = app.window(title='Информация')
# Здесь кнопка Ок на русском
keda_window.Ок.click()

# Погрешнось измерений
pywinauto.mouse.click(button='left', coords=(227, 540))
keda_window = app.window(title='Погрешность измерений')
keda_window.Закрыть.click()
# keda_window.Погрешностьизмерений.click()

# Параметры ППД
pywinauto.mouse.click(button='left', coords=(183, 611))
keda_window = app.window(title='Параметры детектора')
keda_window.Отменить.click()
# keda_window.ПараметрыППД.click()

# Измерение спектров
pywinauto.mouse.click(button='left', coords=(235, 684))
keda_window = app.window(title='Программа качественного анализа')
keda_window.tbExit.click()
# keda_window.Измерениеспектров.click()

# Интенсиметр
pywinauto.mouse.click(button='left', coords=(224, 749))
keda_window = app.window(title='Интенсиметр')
keda_window.close()
# keda_window.Интенсиметр.click()

# Паспортные характеристики
pywinauto.mouse.click(button='left', coords=(195, 811))
keda_window = app.window(title='Измерение паспортных характеристик')
keda_window.Закрыть.click()
# keda_window.Паспортныехарактеристики.click()

# Инициализация
# pywinauto.mouse.click(button='left', coords=(232, 883))
# keda_window.Инициализация.click()

# Помощь
# keda_window = app.window(title='Наладка-W БРА-135F')
# keda_window.Помощь.click()
# тоже, что и выше, но координатами
# pywinauto.mouse.click(button='left', coords=(1467, 984))
# keda_window = app.window(title='WidgetMax')
# keda_window.close()

# ниже код работает в окне Наладка-W БРА-135F
keda_window = app.window(title='Наладка-W БРА-135F')
keda_window.Закрыть.click()
keda_window = app.window(title='КЭДА')
keda_window.Выходизпрограммы.click()
keda_window = app.window(title='Подтверждение')
keda_window.Да.click()

# пример задеркжки
# keda_window.wait('visible', timeout='5')
