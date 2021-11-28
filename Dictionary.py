from module1 import *

capitals={"Russia":"Moscow", "Estonia":"Tallinn", "Ukraine":"Kiev", "France":"Paris", "Canada":"Toronto", "Spain":"Madrid"}


while True:
    print(capitals)
    a=input("Поиск столиц и государств - 1\nДобавляем новую столицу и страну - 2\nИсправляем ошибки в словаре - 3\nПроверяем знания - 4\nЗакончить работу - нажмите любую клавишу.\n")
    
    if a=="1":
        b=input("Ищем столицу - 1\nИщем государство - 2\n")
        if b=="1":
            name=input("Введите название государства: ").title()
            answer=capital_search(capitals, a, b, name, choice)
        elif b=="2":
            name=input("Введите название столицы: ").title()
            answer2=capital_search(capitals, a, b, name, choice)

    elif a=="2":
         update=add_new(capitals, new_state, new_city)

    elif a=="3":
        a=input("Что будем исправлять?\nСтраны - 1\nСтолицы - 2?\n")
        if a=="1":
            state_name=input("Введите название страны для исправления: ").title()
            state_correction_1=state_cleanup(capitals, a, state_name)
            state_correction_2=state_update(capitals, state_name)
        if a=="2":
            city_name=input("Введите название столицы для исправления: ").title()
            city_correction=city_cleanup(capitals, a, city_name)
            update=add_new(capitals, new_state, new_city)
            
    elif a=="4":
        quiz=knowledge_check(capitals, answer, counter, answer_state)
    else:
        break

