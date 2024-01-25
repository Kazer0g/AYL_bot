from enum import Enum

class MenuTexts(Enum):
    main_menu = 'Главное меню'
    presenters = 'Штат'
    polls = 'Анкеты'
    poll = 'Анкета'

class ButtonsText(Enum):
    presenters = 'Ведущие'
    send_poll = 'Отправить анкету'
    feedback = 'Посмотреть обратную связь'
    polls = 'К анкетам'

    add_person = 'Добавить человека'
    add_poll = 'Добавить анкету'
    add_question = 'Добавить вопрос'

    back = 'Назад'

    yes = 'Да'
    no = 'Нет'
    
    change_question = 'Изменить вопрос'

    main_menu = 'В главное меню'
    delete = '-'

    thread_1 = '1 поток'
    thread_2 = '2 поток'
    thread_3 = '3 поток'
    thread_junior = 'Юниорская'
    thread_global = 'Глобальная'

    question_type_text = 'Текстовый'
    question_type_1_5 = '1-5'
    question_type_1_10 = '1-10'