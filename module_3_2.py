def send_email(messege, recepient, sender='university.help@gmail.com'):
    at_r = False  # для проверки '@' recepient
    at_s = False  # для проверки '@' sender
    point_r = False  # для проверка точки recepient'.'
    point_s = False  # для проверка точки sender'.'
    domen_r = False  # для проверки домена recepient
    domen_s = False  # для проверки домена sender
    domen_str = ''  # пустая строка для проверки домена

    for i in recepient:
        if i == '@':  # проверка на '@'
            at_r = True
        if at_r == True and i == '.':  # проверка на '.'
            point_r = True
        if point_r == True:  # вписывает всё что после точки
            domen_str = domen_str + i
    domen_list = [domen_str]  # str. меняет в list.

    if '.ru' in domen_list:  # проверка домена recepient
        domen_r = True
    elif '.net' in domen_list:
        domen_r = True
    elif '.com' in domen_list:
        domen_r = True

    domen_str = ''  # обнуляет для проверки sender

    for i in sender:
        if i == '@':  # проверка на '@'
            at_s = True
        if at_s == True and i == '.':  # проверка на '.'
            point_s = True
        if point_s == True:  # вписывает всё что после точки
            domen_str = domen_str + i
    domen_list = [domen_str]  # str. меняет в list.

    if '.ru' in domen_list:  # проверка домена sender
        domen_s = True
    elif '.net' in domen_list:
        domen_s = True
    elif '.com' in domen_list:
        domen_s = True

    email_true = at_r + at_r + domen_r + domen_s + point_r + point_s  # сумма трёх Истин

    if email_true < 6:  # если есть хоть одна Ложь то:
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recepient}')
    if email_true == 6 and recepient == sender:
        print('Нельзя отправить письмо самому себе!')  # если отправитель совпадает с получателем
    elif email_true == 6 and recepient == 'urban.fan@mail.ru':
        print('НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса urban.info@gmail.com на адрес urban.fan@mail.ru')
    elif email_true == 6:
        print(f'Письмо успешно отправлено с адреса <{sender}> на адрес <{recepient}>!')  # успешная отправка письма

# send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
# send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
# send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
# send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
