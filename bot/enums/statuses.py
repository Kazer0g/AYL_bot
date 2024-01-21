from enum import Enum

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