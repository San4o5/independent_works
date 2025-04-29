
from analysis.helpers import is_number

#Підрахунок кількості чисел у токенах.
def count_digits(tokens):
    count = 0
    for token in tokens:
        if is_number(token):
            count += 1
            
    return count
    
#Підрахунок кількості зміни знаку між числами (позитивне/негативне/нуль)
def alternation_count(tokens):    
    states = []
    
    for token in tokens:
        if is_number(token):
            num = float(token)
            if num > 0:
                states.append('POS')
            elif num < 0:
                states.append('NEG')
            else:
                states.append('ZERO')
    
    if not states:
        return 0
    
    count = 0 #Кількість знакозмін
    for i in range(1, len(states)):
        #Поточний стан числа проти попереднього стану числа
        if states[i] != states[i-1]:
            count += 1
    
    return count
    