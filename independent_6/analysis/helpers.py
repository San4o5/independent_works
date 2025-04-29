
from config import DELIMITERS

#Перевірка, чи є символ роздільником
def is_delimiter(char):
    return char in DELIMITERS

#Перевірка чи є токен числом
def is_number(token):
    try:
        float(token)
        return True
    except ValueError:
        return False
