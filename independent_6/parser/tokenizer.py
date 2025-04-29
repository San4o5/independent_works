from config import DELIMITERS
from analysis.helpers import is_number

#Розбиваємо текст на токени (слова, числа)
def tokenize(text):
    tokens = []
    current_token = '' #Поточне слово
    for char in text:
        if char not in DELIMITERS:
            current_token += char
        else:
            if current_token:
                process_token(current_token, tokens)
                current_token = ''
    
    if current_token:
        process_token(current_token, tokens)
    
    return tokens

#Обробка одного токену, перевіряємо чи це число
def process_token(token, tokens_list):
    if is_number(token):
        try:
            num = float(token)
            tokens_list.append(num)
        except ValueError:
            tokens_list.append(token)
    else:
        tokens_list.append(token)