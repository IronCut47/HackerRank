# This quesiton is solved in "Pypy3" because for some reason it's not passing the tesh case when done in "Python 3"
if __name__ == '__main__':
    n = int(input())
    integer_list = list(map(int, input().split()))
    tup = tuple(integer_list)
    print(hash(tup))