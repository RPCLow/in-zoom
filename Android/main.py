import datetime
import webbrowser
import calendar


settings = {'время_уроков': {'1': {'Начало': '9:00', 'Конец': '9:45'}, '2': {'Начало': '9:55', 'Конец': '10:40'}, '3': {'Начало': '10:50', 'Конец': '11:35'}, '4': {'Начало': '11:55', 'Конец': '12:40'}, '5': {'Начало': '12:50', 'Конец': '13:35'}, '6': {'Начало': '13:45', 'Конец': '14:30'}, '7': {'Начало': '14:40', 'Конец': '15:25'}}, 'расписание': {'Monday': {'1': 'Мистецтво', '2': 'Українська література', '3': 'Алгебра', '4': 'Фізика', '5': 'Географія', '6': 'Геометрія', '7': 'Всесвітня історія'}, 'Tuesday': {'1': 'Громадянська освіта', '2': 'Хімія', '3': 'Зарубіжна література', '4': 'Алгебра', '5': 'Українська мова', '6': 'Англійский', '7': 'Фізична культура'}, 'Wednesday': {'1': 'Українська література', '2': 'Фізика', '3': 'Захист України', '4': 'Географія', '5': 'Геометрія', '6': 'Біологія', '7': 'Алгебра'}, 'Thursday': {'1': 'Громадянська освіта', '2': 'Українська мова', '3': 'Фізика', '4': 'Фізична культура', '5': 'Геометрія', '6': 'Алгебра', '7': 'Інформатика'}, 'Friday': {'1': 'Основи медіаграмотності', '2': 'Фізична культура', '3': 'Біологія', '4': 'Англійский', '5': 'Захист України', '6': 'Алгебра', '7': 'Інформатика'}}, 'ссылка_на_уроки': {'Українська література': None, 'Всесвітня історія': 'https://us04web.zoom.us/j/8315407262?pwd=MGE0aWRpaS9RSDI2bFVPd2JBckZqdz09', 'Громадянська освіта': 'https://us04web.zoom.us/j/75173169119?pwd=MOEU2w9QFdHM8W2pwhbaRqWXl2kb5h.1', 'Хімія': 'https://us04web.zoom.us/j/71638340957?pwd=4eeAchiKkd4KBqwOg7JF8Dzu3mH3YH.1', 'Фізична культура': None, 'Захист України': None, 'Українська мова': None, 'Мистецтво': None, 'Географія': None, 'Біологія': None, 'Фізика': None, 'Алгебра': 'https://us05web.zoom.us/j/89422289385?pwd=UXQycHdXVjd4bDQxS3NzS1JjNklTUT09', 'Геометрія': 'https://us05web.zoom.us/j/89422289385?pwd=UXQycHdXVjd4bDQxS3NzS1JjNklTUT09', 'Зарубіжна література': None, 'Англійский': 'https://us04web.zoom.us/j/75586102781?pwd=0H9X4AjBXrGOzPafdXjEYO7Lv0VcC0.1', 'Інформатика': 'https://us05web.zoom.us/j/83110293882?pwd=tR93tWg0xbOnSVpkuHpc4KFQ45bRSz.1', 'Основи медіаграмотності': 'https://us04web.zoom.us/j/74219303272?pwd=HjmJ9vmOqBb7BQLtlJYbdvbEd7NWjx.1%20%20%D0%98%D0%B4%D0%B5%D0%BD%D1%82%D0%B8%D1%84%D0%B8%D0%BA%D0%B0%D1%82%D0%BE%D1%80%20%D0%BA%D0%BE%D0%BD%D1%84%D0%B5%D1%80%D0%B5%D0%BD%D1%86%D0%B8%D0%B8:%20742%201930%203272%20%D0%9A%D0%BE%D0%B4%20%D0%B4%D0%BE%D1%81%D1%82%D1%83%D0%BF%D0%B0:%20t8YU1h', 'Иначе': 'https://lms.human.ua/app/calendar'}}


текущее_время = datetime.datetime.now().time()
номер_урока = str()
урок_найден = False
for k, v in settings["время_уроков"].items():
    начальное_время = datetime.datetime.strptime(v['Начало'], "%H:%M").time()
    конечное_время = datetime.datetime.strptime(v['Конец'], "%H:%M").time()
    if начальное_время <= текущее_время <= конечное_время:
        номер_урока = k
        урок_найден = True
        break

день_недели = calendar.day_name[datetime.datetime.now().weekday()]
if урок_найден:
    урок_который_идет_сейчас = settings["расписание"][день_недели][номер_урока]
    ссылка_на_zoom = settings["ссылка_на_уроки"][урок_который_идет_сейчас]
    print(f'Сейчас идет урок по {урок_который_идет_сейчас}.')
    if ссылка_на_zoom:
        ответ = input(f'Нажмите Enter что бы подключиться: ')
        if not ответ:
            print(f'Происходит подключение к Zoom для урока {урок_который_идет_сейчас}')
            webbrowser.open_new_tab(ссылка_на_zoom)
            print('Успешно подключились.')
    else:
        ответ = input(f'Ссылки на зум по {урок_который_идет_сейчас} не найдено.\nНапишите "выйти" если хотите выйти или нажмите Enter если хотите подключится к {settings['ссылка_на_уроки']['Иначе']}: ')
        if ответ.lower() != 'выйти':
            print(f'Происходит подключение к Zoom для урока {урок_который_идет_сейчас}')
            webbrowser.open_new_tab(settings['ссылка_на_уроки']['Иначе'])
            print('Успешно подключились.')
        else:
            print('Завершаем работу...')

else:
    print('Уроков сейчас нет, отдохните.')
            
