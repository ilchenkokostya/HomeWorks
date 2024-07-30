def send_email(message, recipient, *, sender="university.help@gmail.com"):
    print("\033[38m",message)

    domens = ['.com', '.ru', '.net']

    if (
            (not any(domen in recipient for domen in domens) or '@' not in recipient)
            or
            (not any(domen in sender for domen in domens) or '@' not in sender)
    ):
        print("\033[31mНевозможно отправить письмио с адреса", sender, "на адрес", recipient)

    elif sender == recipient:
        print( "\033[33mНельзя отправить письмо самому себе!")

    elif sender == "university.help@gmail.com":
        print("\033[32mПисьмо успешно отправлено с адреса", sender,  "на адрес", recipient)
    else:
        print("\033[35mНЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса", sender, "на адрес", recipient)
    print("\033[37m---------")

send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')