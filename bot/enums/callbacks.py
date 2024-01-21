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