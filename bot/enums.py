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
    add_question = 'add_question'

    username_prefix = 'username'
    role_prefix = 'role'
    delete_stuff_prefix = 'delete_stuff'

    poll_id_prefix = 'poll_id'
    poll_name_prefix = 'poll_name'
    delete_poll_prefix = 'delete_poll'

    prefix_divider = ':'
    
    data_divider = '-'


class DialogStatuses(Enum):
    none = 'None'

class Statuses(Enum):
    status_inactive = 'inactive'
    status_active = 'active'

    conference_mode = 'conference'
    static_mode = 'static'

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

    yes = 'Да'
    no = 'Нет'

    main_menu = 'В главное меню'
    delete = '-'