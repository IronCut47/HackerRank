import textwrap

def wrap(string, max_width):
    wrapped = ''
    i = 0
    while i < len(string):
        temp = string[i : i+max_width]
        wrapped += temp + '\n'
        i += max_width
    return wrapped

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)