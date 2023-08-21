def print_formatted(number):
    space = len(bin(number)[2:])
    for i in range(1, number + 1):
        d = str(i).rjust(space)
        o = oct(i)[2:].rjust(space + 1)
        h = hex(i).upper()[2:].rjust(space + 1)
        b = bin(i)[2:].rjust(space + 1)
        print(f'{d}{o}{h}{b}') #Using f-string

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)