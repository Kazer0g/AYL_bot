from enum import Enum


class CallBacks (Enum):
    accept = 'accept'
    reject = 'reject'

    main_menu = 'main_menu'
    presenters = 'presenters'
    send_poll = 'send_poll'
    polls = 'polls'
    feedback = 'feedback'
    add_person = 'add_person'
    add_poll = 'add_poll'
    add_question_prefix = 'add_question'
    set_question_prefix = 'set_question'
    delete_question_prefix = 'delete_question'
    question_prefix = 'question'

    username_prefix = 'username'
    role_prefix = 'role'
    delete_stuff_prefix = 'delete_stuff'

    poll_id_prefix = 'poll_id'
    poll_name_prefix = 'poll_name'
    poll_type_prefix = 'poll_type'
    delete_poll_prefix = 'delete_poll'

    thread_prefix = 'thraed'
    thread_1 = 'thread_1'
    thread_2 = 'thread_2'
    thread_3 = 'thread_3'
    thread_junior = 'thread_junior'
    thread_global = 'thread_global'

    prefix_divider = ':'
    
    data_divider = '-'


class DialogStatuses(Enum):
    none = 'None'

class Statuses(Enum):
    status_inactive = 'inactive'
    status_active = 'active'

    conference_mode = 'conference'
    static_mode = 'static'

    thread_1 = '1'
    thread_2 = '2'
    thread_3 = '3'
    thread_junior = 'junior'
    thread_global = 'global'

class Roles(Enum):
    director = 'director'
    delegate = 'delegate'

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

    back = 'back'

    yes = 'Да'
    no = 'Нет'

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