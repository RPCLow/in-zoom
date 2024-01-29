import datetime
import webbrowser
import calendar


settings = # УДАЛИТЕ КОММЕНТАРИЙ И ВСТАВТЕ ТО, ЧТО ВЫ СКОПИРОВАЛИ


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
        ответ = input(f'Нажмите Enter что бы подключиться. Если вы хотите перезаписать настройки, напишите "Перезаписать": ')
        if not ответ:
            print(f'Происходит подключение к Zoom для урока {урок_который_идет_сейчас}')
            webbrowser.open_new_tab(ссылка_на_zoom)
            print('Успешно подключились.')
        elif ответ.lower() == 'перезаписать':
            os.remove(filename)
            print('Файл с настройками удален!')
            print('Перезапустите скрипт что бы начать настройку сзаного.')
        

else:
    print('Уроков сейчас нет, отдохните.')
            
