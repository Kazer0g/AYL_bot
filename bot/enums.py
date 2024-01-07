from enum import Enum

class CallBacks (Enum):
    main_menu = 'main_menu'
    presenters = 'presenters'
    send_poll = 'send_poll'
    feedback = 'feedback'

class DialogStatuses(Enum):
    a = '0'

class Statuses(Enum):
    status_inactive = 'inactive'
    status_active = 'active'

class Roles(Enum):
    director = 'director'
    delegate = 'delegate'

class Texts(Enum):
    main_menu = 'Главное меню'