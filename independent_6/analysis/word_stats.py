#Підрахунок кількості слів серед токенів.
def count_words(tokens):
    words = []
    for token in tokens:
        if isinstance(token,str): #Перевіряємо чи токен є рядком
            words.append(token)
    
    return len(words)

#Підрахунок кількості слів довжини n.
def count_words_len(tokens, n):
    count = 0
    for token in tokens:
        if isinstance(token,str) and len(token) == n:
            count += 1
    
    return count

#Підрахунок кількості унікальних слів (без врахування регістру)
def count_unique_words(tokens):
    normalized = []
    for token in tokens:
        if isinstance(token,str):
            normalized.append(token.lower())
    
    unique_words = set(normalized)

    return len(unique_words)

#Підрахунок кількості слів, що починаються з великої літери.
def count_titlecase_words(tokens):
    count = 0
    for token in tokens:
        if isinstance(token, str) and token and token[0].isupper():
            count += 1
    
    return count