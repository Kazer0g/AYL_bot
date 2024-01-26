from enum import Enum

class CallBacks (Enum):
    accept = 'accept'
    reject = 'reject'
    
    set_question_type = 'set_question_type'
    question_type_text = 'question_type_text'
    question_type_1_5 = 'question_type_1_5'
    question_type_1_10 = 'question_type1_10'
    change_question = 'change_question'
    change_question_type = 'change_question_type'

    main_menu = 'main_menu'
    presenters = 'presenters'
    send_poll = 'send_poll'
    polls = 'polls'
    feedback = 'feedback'
    add_person = 'add_person'
    add_poll = 'add_poll'
    add_question = 'add_question'
    set_question_prefix = 'set_question'
    delete_question_prefix = 'delete_question'
    question_prefix = 'question'
    
    poll_name = 'change_poll_name'
    poll_type = 'change_poll_type'

    username_prefix = 'username'
    role_prefix = 'role'
    delete_stuff_prefix = 'delete_stuff'
    

    poll_id_prefix = 'poll_id'
    poll_name_prefix = 'poll_name'
    poll_type_prefix = 'poll_type'
    delete_poll_prefix = 'delete_poll'
    
    delete = 'delete'
    poll = 'poll'
    question = 'question'
    
    answer = 'answer'

    thread_prefix = 'thraed'
    thread_1 = 'thread_1'
    thread_2 = 'thread_2'
    thread_3 = 'thread_3'
    thread_junior = 'thread_junior'
    thread_global = 'thread_global'

    prefix_divider = ':'
    divider = ':'
    
    data_divider = '-'