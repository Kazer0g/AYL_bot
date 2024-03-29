BOT_DESCRIPRION = 'HI'
GREETINGS_FOR_DIRECTOR = 'Hi, director'
GREETINGS_FOR_DELEGATE = 'Hi, delegate'

def delete_from_stuff_message_generator(username, role):
    return f'Вы уверенны что хотите удалить {username} из персонала? Роль будет изменена на {role}.'

def delete_from_polls_message_generator(poll_name):
    return f'Вы уверены что хотите удалить {poll_name} из списка анкет?'

def answer_message_generator(poll_name, answers):
    message = poll_name
    for answer in answers:
        message += f'\n{answer[0]}: {answer[1]}'
    return message

ADD_QUESTION = 'Введите формулировку вопроса'
SELECT_QUESTION_TYPE = 'Выберите тип ответа на вопрос'
WRITE_POLL_NAME = 'Введите название анкеты'
SELECT_POLL_TYPE = 'Выберите тип анкеты'
DELETE_QUESTION = 'Удалить вопрос?'
SEND_POLL = 'Отправить анкету?'
ANSWER = 'Введите ответ'