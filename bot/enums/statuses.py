from enum import Enum


class DialogStatuses(Enum):
    none = "None"
    start = "start"
    main_menu = "main_menu"
    polls = "polls"
    poll = "poll"
    add_poll = "add_poll"
    poll_name = "change_poll_name"
    poll_type = "change_poll_type"
    question = "question"
    set_question = "set_question"
    set_question_type = "set_question_type"
    change_question_type = "change_question_type"
    change_question = "change_question"
    delete = "delete"
    presenters = "presenters"
    divider = ":"


class Statuses(Enum):
    status_inactive = "inactive"
    status_active = "active"

    conference_mode = "conference"
    static_mode = "static"

    thread_1 = "1"
    thread_2 = "2"
    thread_3 = "3"
    thread_junior = "junior"
    thread_global = "global"

    type_text = "text"
    type_1_5 = "1-5"
    type_1_10 = "1-10"


class Roles(Enum):
    director = "director"
    delegate = "delegate"
