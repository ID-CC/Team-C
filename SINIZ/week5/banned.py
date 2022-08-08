import re
from itertools import  product

def solution(user_id, banned_id):
    answer_list = list()
    banned_list = []
    banned_length = len(banned_id)
    
    for banned in banned_id:
        banned = banned.replace("*", ".")
        p = re.compile(banned)
        id_list = []
    
        for user in user_id:
            if len(banned) == len(user) and p.match(user):
                id_list.append(user)
        banned_list.append(id_list)
        
    for candidate in product(*banned_list): # 포인터 아닙니다. 
        candidate = set(candidate)
        if len(candidate) == banned_length and candidate not in answer_list:
            answer_list.append(candidate)
    return len(answer_list)
