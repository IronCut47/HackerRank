if __name__ == '__main__':
    s = input()
    knowledge = {'isalnum' : False, 'isalpha' : False, 'isdigit' : False, 'islower' : False,   'isupper' : False}
    
    for char in s:
        if char.isalnum():
            knowledge['isalnum'] = True
        if char.isalpha():
            knowledge['isalpha'] = True
        if char.isdigit():
            knowledge['isdigit'] = True
        if char.islower():
            knowledge['islower'] = True
        if char.isupper():
            knowledge['isupper'] = True
    
    for i in knowledge:
        print(knowledge[i])