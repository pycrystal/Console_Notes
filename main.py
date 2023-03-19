from art import tprint
import pickle
from simple_term_menu import TerminalMenu

#Красивая надпись
tprint('Notes')

#Главное меню
choise = ['1 - Посмотреть заметки', '2 - Добавить заметку', '3 - Выход']
user_input = TerminalMenu(choise, title="Команды:")
user_input.show()


#Что-бы сохранить
while True:
    monday = ''
    tuesday = ''
    wednesday = ''
    thursday = ''
    friday = ''
    saturday = ''
    sunday = ''

    #Меню для записи заметок
    if user_input.chosen_menu_index == 1:
        num = ['1 - Понедельник', '2 - Вторник', '3 - Среда', '4 - Четверг', '5 - Пятница', '6 - Суббота', '7 - Воскресенье']
        menu = TerminalMenu(num, title="Выберите день недели:")
        menu.show()
        
        #Понедельник
        if menu.chosen_menu_index == 0:
            monday = input()
            f = open('mon.bin', 'wb')
            pickle.dump(monday, f)
            f.close()
            choise = ['1 - Посмотреть заметки', '2 - Добавить заметку', '3 - Выход']
            user_input = TerminalMenu(choise, title="Команды:")
            user_input.show()

        #Вторник     
        elif menu.chosen_menu_index == 1:
            tuesday = input()
            f = open('tue.bin', 'wb')
            pickle.dump(tuesday, f)
            f.close()
            choise = ['1 - Посмотреть заметки', '2 - Добавить заметку', '3 - Выход']
            user_input = TerminalMenu(choise, title="Команды:")
            user_input.show()

        #Среда
        elif menu.chosen_menu_index == 2:
            wednesday = input() 
            f = open('wed.bin', 'wb')
            pickle.dump(wednesday, f)
            f.close()  
            choise = ['1 - Посмотреть заметки', '2 - Добавить заметку', '3 - Выход']
            user_input = TerminalMenu(choise, title="Команды:")
            user_input.show()  

        #Четверг      
        elif menu.chosen_menu_index == 3:
            thursday = input()
            f = open('thu.bin', 'wb')
            pickle.dump(thursday, f)
            f.close()
            choise = ['1 - Посмотреть заметки', '2 - Добавить заметку', '3 - Выход']
            user_input = TerminalMenu(choise, title="Команды:")
            user_input.show()

        #Пятница
        elif menu.chosen_menu_index == 4:
            friday = input()
            f = open('fri.bin', 'wb')
            pickle.dump(friday, f)
            f.close()
            choise = ['1 - Посмотреть заметки', '2 - Добавить заметку', '3 - Выход']
            user_input = TerminalMenu(choise, title="Команды:")
            user_input.show()

        #Суббота
        elif menu.chosen_menu_index == 5:
            saturday = input()
            f = open('sat.bin', 'wb')
            pickle.dump(saturday, f)
            f.close()
            choise = ['1 - Посмотреть заметки', '2 - Добавить заметку', '3 - Выход']
            user_input = TerminalMenu(choise, title="Команды:")
            user_input.show()

        #Воскресенье
        elif menu.chosen_menu_index == 6:
            sunday = input()
            f = open('sun.bin', 'wb')
            pickle.dump(sunday, f)
            f.close()   
            choise = ['1 - Посмотреть заметки', '2 - Добавить заметку', '3 - Выход']
            user_input = TerminalMenu(choise, title="Команды:")
            user_input.show()   

    #Меню для вывода заметок
    if user_input.chosen_menu_index == 0:
        num = ['1 - Понедельник', '2 - Вторник', '3 - Среда', '4 - Четверг', '5 - Пятница', '6 - Суббота', '7 - Воскресенье']
        menu = TerminalMenu(num, title="Выберите день недели:")
        menu.show()

        #Понедельник
        if menu.chosen_menu_index == 0:
            tprint('Monday')
            f = open('mon.bin', 'rb')
            monday_output = pickle.load(f)
            print(monday_output)
            f.close()
            choise = ['1 - Посмотреть заметки', '2 - Добавить заметку', '3 - Выход']
            user_input = TerminalMenu(choise, title="Команды:")
            user_input.show()

        #Вторник
        elif menu.chosen_menu_index == 1:
            tprint('Tuesday')
            f = open('tue.bin', 'rb')
            tuesday_output = pickle.load(f)
            print(tuesday_output)
            f.close()
            choise = ['1 - Посмотреть заметки', '2 - Добавить заметку', '3 - Выход']
            user_input = TerminalMenu(choise, title="Команды:")
            user_input.show()

        #Среда
        elif menu.chosen_menu_index == 2:
            tprint('Wednesday')
            f = open('wed.bin', 'rb')
            wednesday_output = pickle.load(f)
            print(wednesday_output)
            f.close()
            choise = ['1 - Посмотреть заметки', '2 - Добавить заметку', '3 - Выход']
            user_input = TerminalMenu(choise, title="Команды:")
            user_input.show()

        #Четверг
        elif menu.chosen_menu_index == 3:
            tprint('Thursday')
            f = open('thu.bin', 'rb')
            thursday_output = pickle.load(f)
            print(thursday_output)
            f.close()
            choise = ['1 - Посмотреть заметки', '2 - Добавить заметку', '3 - Выход']
            user_input = TerminalMenu(choise, title="Команды:")
            user_input.show()

        #Пятница  
        elif menu.chosen_menu_index == 4:
            tprint('Friday')
            f = open('fri.bin', 'rb')
            friday_output = pickle.load(f)
            print(friday_output)
            f.close()
            choise = ['1 - Посмотреть заметки', '2 - Добавить заметку', '3 - Выход']
            user_input = TerminalMenu(choise, title="Команды:")
            user_input.show()

        #Суббота
        elif menu.chosen_menu_index == 5:
            tprint('Saturday')
            f = open('sat.bin', 'rb')
            saturday_output = pickle.load(f)
            print(saturday_output)
            f.close()
            choise = ['1 - Посмотреть заметки', '2 - Добавить заметку', '3 - Выход']
            user_input = TerminalMenu(choise, title="Команды:")
            user_input.show()

        #Воскресенье
        elif menu.chosen_menu_index == 6:
            tprint('Sunday')
            f = open('sun.bin', 'rb')
            sunday_output = pickle.load(f)
            print(sunday_output)
            f.close()
            choise = ['1 - Посмотреть заметки', '2 - Добавить заметку', '3 - Выход']
            user_input = TerminalMenu(choise, title="Команды:")
            user_input.show() 

     #Выход       
    if user_input.chosen_menu_index == 2:
        break 
