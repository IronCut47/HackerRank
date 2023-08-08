if __name__ == '__main__':
    N = int(input())
    follow = {}
    new = []
    
    for i in range(0, N):
        command = str(input())
        
        com, *line = command.split() # splits first word and assign it to com as type(Str)".." and rest to line as type(list[...]).
        num = list(map(int, line)) # Assigns elements in line to num[].
        follow[com] = num # Updating dictonary with 'com' and 'num'. 
        
        if com == "insert":
            new.insert(num[0], num[1])
        elif com == "remove":
            new.remove(num[0])
        elif com == 'append':
            new.append(num[0])
        elif com == 'sort':
            new.sort()
        elif com == 'pop':
            new.pop()
        elif com == 'reverse':
            new.reverse()
        elif com == 'print':
            print(new)