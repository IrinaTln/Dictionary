import random

state=""
new_state=""
new_city=""
choice=""
answer=""
answer_state=""
counter=""



def capital_search(capitals:str, a:str,b:str, name:str, choice:str): #Поиск в словаре столицы или страны по выбору пользователя 
    """Finding name of capital or state:
        a:str and b:str - user input
        capital_name:str and state_name:str - user input
    """
    state=""

    if b=="1":
        state_key=capitals.get(name)
        print(state_key)
        if state_key==None:
            choice=input("Такое значение не найдено.\nХотите добавить новую столицу - 1?\nВыход - 2?\n")
            if choice=="1":
                add_new(capitals, new_state, new_city)              
                           

    elif b=="2":
        for key, value in capitals.items():
            if value==name:
                state=key
                print(state)
        right_city=capitals.get(state)
        print(right_city)
        if right_city!=name:
            choice= input("Такое значение не найдено.\nХотите добавить новое государство - 1?\nВыход - 2?")
            if choice=="1":
                add_new(capitals, new_state, new_city)

           

def add_new (capitals:str, new_state:str, new_city:str): #Добавляем в словрь новую пару ключ и значение
    """Input new key and value in dictionary.
        Capitals:str as a dictionary, new_state:str - name of key
        new_city:str - value.
    """
    new_state=str(input("Введите название государства: ")).title()
    new_city=str(input("Введите название столицы: ")).title()
    capitals[new_state]=new_city
    print("Поздравляю! Вы добавили в словарь новую пару. Теперь ваш словарь выглядит так: ", capitals)
    return capitals

def state_cleanup(capitals:str, a:str, state_name:str): #Очищаем словарь от пары страна-столица по имени страны
    """Deleting key-value from dictionary
        capitals:str as a dictionary, a:str - user choice, name:str as dictionary key
    """
    if state_name in capitals:
        del(capitals[state_name])
        print("Поздравляем! Исправление прошло успешно. Давайте теперь обновим наш словарь.")
        print(capitals)
    else:
        print("Такой страны в словаре нет!Давайте его обновим.")
    return capitals

def state_update (capitals:str, state_name:str): #Проверяем наличие страны в словаре и добавляем, если такой нет
    if state_name in capitals:
        print("Будте внимательны! Такая стране в словаре уже есть.")
    else:
        add_new(capitals, new_state, new_city)

def city_cleanup(capitals:str, a:str, city_name:str): #Удаляем из словаря пару страна-столица по столице.
    """Deleting from the dictionary item key-value by value
       capitals:str as dictionary, a:str - user choice, name:str - as value
    """
    for state, capital in capitals.items():
        if capital==city_name:
            state_key=state
    del(capitals[state_key])
    print("Поздравляем! Исправление прошло успешно. Давайте теперь обновим наш словарь.")
    return capitals
    
    add_new (capitals, new_state, new_city)

def knowledge_check(capitals:dict, answer:str, counter:int, answer_state:str): #Провека знаний пользователя
    """Checking user knowladge by city and state in random order
    """
    
    print("Вам дается шесть вопросов. В конце - общий зачет.")
    counter=0 #счетчик правильных ответов
    i=0 #количество раундов
    
    while i<3: 
        test_state=random.choice(list(capitals.keys()))
        print(test_state)
        answer=input("Введите название столицы: ").title()
        correct_answer=capitals.get(test_state)
        print(correct_answer)
        if answer==correct_answer:
            print("Поздравляем! Это правильный ответ!")
            counter+=1
        else:
            print("Пичалька!Ответ не верный.")
        test_city=random.choice(list(capitals.values()))
        print(test_city)
        answer_state=input("Введите название государства: ").title()
        correct_city_name=capitals.get(answer_state)
        if correct_city_name==test_city:
            print("Поздравляем! Это правильный ответ!")
            counter+=1
        else:
            print("Пичалька! Ответ не верный.")

        i+=1
    if counter==6:
        print("100% попаданий! Вы отлично знаете географию.")
    elif counter<4:
        print("У вас достаточно знаний, чтобы не заблудиться на планете.")
    elif counter<2:
        print("Имеет смысл подучить геогарафию! :-)")
    else:
        print("Вы тестировщик и проверяли работу счетчика результатов.")
 
