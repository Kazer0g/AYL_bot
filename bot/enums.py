from enum import Enum

class CallBacks (Enum):
    a = '0'

class DialogStatuses(Enum):
    a = '0'

class Statuses(Enum):
    status_inactive = 'inactive'
    status_active = 'active'

class Roles(Enum):
    director = 'director'
    delegate = 'delegate'