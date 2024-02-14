import datetime
import webbrowser
import calendar
import json
import os

filename = 'settings.json'

current_directory = os.path.dirname(os.path.abspath(__file__))

full_path = os.path.join(current_directory, filename)

if not os.path.isfile(full_path):
    print('Привет! Скорее всего ты уже почитал об этом скрипте на GitHub, но если нет, тогда обьясню коротко.')
    print('Это настраиваемый скрипт, который сам подключает тебя к учебный ссылкам Zoom')
    print('От тебя лишь требуется только активировать скрипт в период урока, что бы скрипт перенес вас по ссылке.')
    input('Итак, так как скрипт у вас еще не настроен, предлагаю перейти к его настройке. Нажмите клавишу Enter для продолжения: ')


    print('----------------------------------------------------')

    print('Сейчас вам нужно будет 1 раз настроить скрипт, после чего, вы сможете им неоднократно пользоваться\n'
        'Примичание: Ссылки на Zoom делятся на Статические и Динамические.\n'
        'Статические - это ссылки, которые не обновляются, то есть тебе один раз дали ссылку на Zoom и ты ей пользуешься.\n'
        'Динамические - это ссылки, которые постоянно обновляются, то есть каждый раз тебе нужно искать новую ссылку на Zoom.')

    print('----------------------------------------------------')

    количество_уроков_в_день = int(input('Итак, давайте определимся с тем, сколько уроков у вас в день. Введите число: '))

    print('----------------------------------------------------')

    while (сколько_дней_в_неделю_учишься := int(input('Введите сколько дней в неделю вы учитесь? Введите число: '))) > 7:
        print(f'В неделе 7 дней, как ты можешь учиться {сколько_дней_в_неделю_учишься} раз в неделю?')

    print('----------------------------------------------------')

    print('Хорошо, теперь давайте определимся с временем начала уроков.')
    время_уроков = {}
    for i in range(1, количество_уроков_в_день + 1):
        время_и_конец_урока = input(f'Напишите через пробел время начало и конца {i} урока. (Пример 9:00 9:45): ').split()
        время_уроков[str(i)] = {'Начало': время_и_конец_урока[0], 'Конец': время_и_конец_урока[1]}

    print('----------------------------------------------------')

    print('Пришло время для расписания.')
    print('----------------------ВНИМАНИЕ----------------------')
    print('Один и тот же урок должен быть написан одинаково, например: Математика и Математика')
    print('Неправильно будет если вы напишите: Математика и математика')
    print('Почему неправильно? Это будет считатся за 2 разных уроков, а соответсвенно, вам нужно будет писать ссылку 2 раза.')
    дни_недели = ['Понедельника', 'Вторника', 'Среды', 'Четверга', 'Пятницы', 'Субботы', 'Воскресенья']
    дни_недели_англ = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    расписание = {}
    уроки = set()

    for i in range(сколько_дней_в_неделю_учишься):
        print(f'Напишите расписание для уроков для {дни_недели[i]}.')
        расписание_дня = {}
        for j in range(1, количество_уроков_в_день + 1):
            имя_урока = input(f'Напишите название {j} урока: ')
            уроки.add(имя_урока)
            расписание_дня[str(j)] = имя_урока
        расписание[дни_недели_англ[i]] = расписание_дня

    print('----------------------------------------------------')

    print('Финальный этап. Сейчас вам нужно будет написать ссылку зум для каждого из уроков.')
    print('Если ссылка Динамическая(смотрите начало), тогда нажмите Enter.')
    ссылка_на_уроки = {}
    for i in уроки:
        ссылка = input(f'Введите ссылку на предмет {i}: ')
        if ссылка:
            ссылка_на_уроки[i] = ссылка
        else:
            ссылка_на_уроки[i] = None
    
    ссылка_на_уроки['Иначе'] = input('Введите ссылку, которая будет открываться если ссылка не будет найдена(Для Human это https://lms.human.ua/app/calendar): ')

    # Создание JSON файла с настройками
    settings = {}
    settings['время_уроков'] = время_уроков
    settings['расписание'] = расписание
    settings['ссылка_на_уроки'] = ссылка_на_уроки

    with open('settings.json', 'w', encoding='UTF-8') as json_file:
        json.dump(settings, json_file, ensure_ascii=False, indent=2)
    print('Все готово! Поздравляю!')
    print('Теперь вы в любое время можете активировать скрипт и подключиться к нужной ссылке!')
    print('Запустите скрипт еще раз если вам нужно прямо сейчас подключиться к Zoom.')



elif os.path.isfile(full_path):
    with open(full_path, 'r', encoding='UTF-8') as json_file:
        settings = json.load(json_file)
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
        иначе = settings['ссылка_на_уроки']['Иначе']
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
            ответ = input(f'Ссылки на урока по {урок_который_идет_сейчас} нет. Нажмите Enter что бы подключиться к {иначе}.\nЕсли вы хотите перезаписать настройки, напишите "Перезаписать": ')
            if not ответ:
                print(f'Происходит подключение к Zoom для урока {урок_который_идет_сейчас}')
                webbrowser.open_new_tab(иначе)
                print('Успешно подключились.')
            elif ответ.lower() == 'перезаписать':
                os.remove(filename)
                print('Файл с настройками удален!')
                print('Перезапустите скрипт что бы начать настройку сзаного.') 

    else:
        print('Уроков сейчас нет, отдохните.')
                
