def split_and_join(line):
    temp = line.split(" ") # Converts given input into a list of strings.
    temp = "-".join(temp) # joing a string with "-" between words.
    return temp

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)