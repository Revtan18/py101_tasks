"""
Программа оценивает сложность пароля.

Пользователь вводит пароль, в ответ получает оценку "сложный"/"простой"
Сложным считается пароль, состоящий как минимум из 8-ми символов,
включая цифры и алфавитные символы
"""

if __name__ == '__main__':
    count = [0,0,0]
    while count != [1,1,1]:
        password = input("Введите пароль:")
        if len(password) < 8:
            print ("Пароль должен иметь не менее 8 символов")  
        else:
            count[0] = 1
        control = any(i for i in password if i.isupper() == True)
        if control == False:
            print("Пароль должен иметь хотя бы одну заглавную букву")
        else:
            count[1] = 1
        control = any(i for i in password if i.isdigit() == True)
        if control == False:
            print("Пароль должен иметь хотя бы одну цифру")
        else:
            count[2] = 1

    print("Пароль соответствует всем критериям сложности!")
