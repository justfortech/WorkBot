from random import choice, randint

answer_list = [
'Что с валовкой брат?',
'Доброе, Поросëночек ;)',
'Зайди к Оле!',
'Фактуры будут?',
'Чë ты лысый плаки плаки?',
'С такой валовкой то...',
'Сомнительно.',
'Я бы на твоëм месте так не радовался.',
'Готов покорять вершины сегодня?',
'Серьëзно?',
'А ты докажи',
'Пнуть, или сам взбодришься?',
'Поживём увидем.',
'Ну ты конь внатуре лось',
'Ты ещё работаешь чтоли?',
'А в тюрьме сейчас ужин, макароны',
'Ну что граждане алкоголики, кто готов поработать',
'Да что вы все такие вежливые аж бесит',
]


sticker_list = [
"CAACAgIAAyEFAASFMqiDAAIGpmazIDdpmdGQpGkK2rTI-QiVvu8OAAJoAQACUomRI53qQjsP3UDlNQQ",

]

def get_answer():
    return choice(answer_list)

def get_sticker():
    return choice(sticker_list)
