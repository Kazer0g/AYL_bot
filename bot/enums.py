from enum import Enum


class CallBacks (Enum):
    main_menu = 'main_menu'
    presenters = 'presenters'
    send_poll = 'send_poll'
    feedback = 'feedback'
    add_person = 'add_person'
    username_prefix = 'username'
    role_prefix = 'role'
    delete_prefix = 'delete'
    prefix_divider = ':'
    
    data_divider = '-'


class DialogStatuses(Enum):
    none = 'None'

class Statuses(Enum):
    status_inactive = 'inactive'
    status_active = 'active'

class Roles(Enum):
    director = 'director'
    delegate = 'delegate'

class MenuTexts(Enum):
    main_menu = 'Главное меню'
    presenters = 'Штат'

class ButtonsText(Enum):
    presenters = 'Ведущие'
    send_poll = 'Отправить анкету'
    feedback = 'Посмотреть обратную связь'

    add_person = 'Добавить человека'

    main_menu = 'В главное меню'