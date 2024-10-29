
values_to_nots = {

    'a': 'до1',
    'b': 'ре1',
    'c': 'ми1',
    'd': 'фа1',
    'e': 'соль1',
    'f': 'ля1',
    'g': 'си1',
    'h': 'до2',
    'i': 'ре2',
    'j': 'ми2',
    'k': 'фа2',
    'l': 'соль2',
    'm': 'ля2',
    'n': 'си2',
    'o': 'до3',
    'p': 'ре3',
    'q': 'ми3',
    'r': 'фа3',
    's': 'соль3',
    't': 'ля3',
    'u': 'си3',
    'v': 'до4',
    'w': 'ре4',
    'x': 'ми4',
    'y': 'фа4',
    'z': 'соль4',

    'а': 'си',
    'б': 'ля',
    'в': 'соль',
    'г': 'фа',
    'д': 'ми',
    'е': 'ре',
    'ё': 'до',
    'ж': 'СИ',
    'з': 'ЛЯ',
    'и': 'СОЛЬ',
    'й': 'ФА',
    'к': 'си4',
    'л': 'МИ',
    'м': 'РЕ',
    'н': 'ДО',
    'о': 'СИ1',
    'п': 'ЛЯ1',
    'р': 'СОЛЬ1',
    'с': 'ФА1',
    'т': 'МИ1',
    'у': 'РЕ1',
    'ф': 'ДО1',
    'х': 'СИ2',
    'ц': 'ЛЯ2',
    'ч': 'ЛЯ2#',
    'ш': 'ДО1#',
    'щ': 'РЕ1#',
    'ъ': 'ФА1#',
    'ы': 'СОЛЬ1#',
    'ь': 'ЛЯ1#',
    'э': 'ДО#',
    'ю': 'РЕ#',
    'я': 'ФА#',

    ' ': 'СОЛЬ#',
    ',': 'ЛЯ#',
    '.': 'до#',
    ':': 'ре#',
    '?': 'фа#',
    '!': 'соль#',
    '-': 'ля#',
    '_': 'до3#',
    "'": 'ре3#',
    '/': 'фа3#',
    '(': 'соль3#',
    ')': 'ля3#',
    ';': 'до4#',
    '+': 'ре4#',
    '=': 'фа4#',
    '"': 'соль4#',
    '<': 'ля4',
    '>': 'ля4#',

    # свободно до5

    '1': 'до1#',
    '2': 'ре1#',
    '3': 'фа1#',
    '4': 'соль1#',
    '5': 'ля1#',
    '6': 'до2#',
    '7': 'ре2#',
    '8': 'фа2#',
    '9': 'соль2#',
    '0': 'ля2#'

}


def encrtypt(input_text):
    encrypted_text = ''
    for i in input_text.lower():
        if i in values_to_nots.keys():
            encrypted_text += values_to_nots[i] + ' '
        else:
            encrypted_text += ' '
    return encrypted_text


def decrypt(input_text: str):
    input_text = input_text.split()
    decrypted_text = ''
    for i in input_text:
        if i in values_to_nots.values():
            keys = list(values_to_nots.keys())
            for j in keys:
                if values_to_nots[j] == i:
                    decrypted_text += j
        else:
            pass
    return decrypted_text


# Если символа нет, то он просто не кодируется.
# Весь русский, английский алфавиты, цифры 0-9 и большинство спец.символов.
# Все слова при дешифровке выводятся в малом регистре

