BOT_DESCRIPRION = 'HI'
GREETINGS_FOR_DIRECTOR = 'Hi, director'
GREETINGS_FOR_DELEGATE = 'Hi, delegate'

def delete_from_stuff_message_generator(username, role):
    return f'Вы уверенны что хотите удалить {username} из персонала? Роль будет изменена на {role}.'

def delete_from_polls_message_generator(poll_name):
    return f'Вы уверены что хотите удалить {poll_name} из списка анкет?'