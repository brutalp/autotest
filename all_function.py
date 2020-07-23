PASSWORD = '0'


def login(app):
    try:
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
        return 'login Ok'
    except:
        pass
