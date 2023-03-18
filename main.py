from art import tprint
import pickle

#Красивая надпись
tprint('Notes')

#Главное меню
print('Команды:\n1 - Посмотреть заметки\n2 - Добавить заметку\n3 - Выход')
user_input = int(input())

#Что-бы сохранить
while True:
    monday = 'input()'
    tuesday = 'input()'
    wednesday = 'input()'
    thursday = 'input()'
    friday = 'input()'
    saturday = 'input()'
    sunday = 'input()'

    #Меню для записи заметок
    if user_input == 2:
        user_day = int(input('Выберите день недели:\n\t1 - Понедельник\n\t2 - Вторник\n\t3 - Среда\n\t4 - Четверг\n\t5 - Пятница\n\t6 - Суббота\n\t7 - Воскресенье\n'))
        #Понедельник
        if user_day == 1:
            monday = input()
            f = open('mon.bin', 'wb')
            pickle.dump(monday, f)
            f.close()
            print('\nКоманды:\n1 - Посмотреть заметки\n2 - Добавить заметку\n3 - Выход')
            user_input = int(input())
        #Вторник     
        elif user_day == 2:
            tuesday = input()
            f = open('tue.bin', 'wb')
            pickle.dump(tuesday, f)
            f.close()
            print('\nКоманды:\n1 - Посмотреть заметки\n2 - Добавить заметку\n3 - Выход')
            user_input = int(input())
        #Среда
        elif user_day == 3:
            wednesday = input() 
            f = open('wed.bin', 'wb')
            pickle.dump(wednesday, f)
            f.close()  
            print('\nКоманды:\n1 - Посмотреть заметки\n2 - Добавить заметку\n3 - Выход')
            user_input = int(input())  
        #Четверг      
        elif user_day == 4:
            thursday = input()
            f = open('thu.bin', 'wb')
            pickle.dump(thursday, f)
            f.close()
            print('\nКоманды:\n1 - Посмотреть заметки\n2 - Добавить заметку\n3 - Выход')
            user_input = int(input())
        #Пятница
        elif user_day == 5:
            friday = input()
            f = open('fri.bin', 'wb')
            pickle.dump(friday, f)
            f.close()
            print('\nКоманды:\n1 - Посмотреть заметки\n2 - Добавить заметку\n3 - Выход')
            user_input = int(input())
        #Суббота
        elif user_day == 6:
            saturday = input()
            f = open('sat.bin', 'wb')
            pickle.dump(saturday, f)
            f.close()
            print('\nКоманды:\n1 - Посмотреть заметки\n2 - Добавить заметку\n3 - Выход')
            user_input = int(input())
        #Воскресенье
        elif user_day == 7:
            sunday = input()
            f = open('sun.bin', 'wb')
            pickle.dump(sunday, f)
            f.close()   
            print('\nКоманды:\n1 - Посмотреть заметки\n2 - Добавить заметку\n3 - Выход')
            user_input = int(input())     
    #Меню для вывода заметок
    if user_input == 1:
        user_out = int(input('Выберите день недели:\n\t1 - Понедельник\n\t2 - Вторник\n\t3 - Среда\n\t4 - Четверг\n\t5 - Пятница\n\t6 - Суббота\n\t7 - Воскресенье\n'))
        #Понедельник
        if user_out == 1:
            tprint('Monday')
            f = open('mon.bin', 'rb')
            monday_output = pickle.load(f)
            print(monday_output)
            f.close()
            print('\nКоманды:\n1 - Посмотреть заметки\n2 - Добавить заметку\n3 - Выход')
            user_input = int(input())
        #Вторник
        elif user_out == 2:
            tprint('Tuesday')
            f = open('tue.bin', 'rb')
            tuesday_output = pickle.load(f)
            print(tuesday_output)
            f.close()
            print('\nКоманды:\n1 - Посмотреть заметки\n2 - Добавить заметку\n3 - Выход')
            user_input = int(input())
        #Среда
        elif user_out == 3:
            tprint('Wednesday')
            f = open('wed.bin', 'rb')
            wednesday_output = pickle.load(f)
            print(wednesday_output)
            f.close()
            print('\nКоманды:\n1 - Посмотреть заметки\n2 - Добавить заметку\n3 - Выход')
            user_input = int(input()) 
        #Четверг
        elif user_out == 4:
            tprint('Thursday')
            f = open('thu.bin', 'rb')
            thursday_output = pickle.load(f)
            print(thursday_output)
            f.close()
            print('\nКоманды:\n1 - Посмотреть заметки\n2 - Добавить заметку\n3 - Выход')
            user_input = int(input())
        #Пятница  
        elif user_out == 5:
            tprint('Friday')
            f = open('fri.bin', 'rb')
            friday_output = pickle.load(f)
            print(friday_output)
            f.close()
            print('\nКоманды:\n1 - Посмотреть заметки\n2 - Добавить заметку\n3 - Выход')
            user_input = int(input())
        #Суббота
        elif user_out == 6:
            tprint('Saturday')
            f = open('sat.bin', 'rb')
            saturday_output = pickle.load(f)
            print(saturday_output)
            f.close()
            print('\nКоманды:\n1 - Посмотреть заметки\n2 - Добавить заметку\n3 - Выход')
            user_input = int(input())
        #Воскресенье
        elif user_out == 7:
            tprint('Sunday')
            f = open('sun.bin', 'rb')
            sunday_output = pickle.load(f)
            print(sunday_output)
            f.close()
            print('\nКоманды:\n1 - Посмотреть заметки\n2 - Добавить заметку\n3 - Выход')
            user_input = int(input()) 
     #Выход       
    if user_input == 3:
        break        