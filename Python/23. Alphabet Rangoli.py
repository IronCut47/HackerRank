import string
alpha = list(string.ascii_lowercase)

def print_rangoli(size):
    temp = (size*2) - 1
    temp = (temp*2) - 1
    
    for i in range(size - 1, -1, -1):
        res1 = alpha[size - 1 : i : -1] + alpha[2 + i : size]
        if len(res1) != 0:
            print('-'.join(res1).center(temp, '-'))
        
    res2 = alpha[size - 1 :  : -1] + alpha[1: size]
    print('-'.join(res2))
    
    for i in range(size):
        res3 = alpha[size - 1 : i : -1] + alpha[2 + i : size]
        if len(res3) != 0:
            print('-'.join(res3).center(temp, '-'))
    
    
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)